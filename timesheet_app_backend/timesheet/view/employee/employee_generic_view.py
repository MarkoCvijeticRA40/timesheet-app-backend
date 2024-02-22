import random
import string
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from timesheet_app_backend.timesheet.model.employee import Employee
from timesheet_app_backend.timesheet.page_number_pagination import CustomPageNumberPagination
from timesheet_app_backend.timesheet.serializer.employee_serializer import EmployeeSerializer
from decouple import config

class EmployeeGenericView(GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = queryset.filter(id=pk)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'pk' in kwargs:
            try:
                print(kwargs['pk'])
                instance = queryset.get(pk=kwargs['pk'])
                serializer = self.serializer_class(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Employee.DoesNotExist:
                return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        page_param = request.query_params.get('page')
        if page_param is not None:
            queryset = self.paginate_queryset(queryset)
            if queryset is not None:
                serializer = self.serializer_class(queryset, many=True)
                return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            send_mail(
                "Welcome to timesheet app!",
                f"Your password is: {random_password}",
                "markopraksa@gmail.com",
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            serializer.validated_data['password'] = random_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            random_password = get_random_string(length=12)
            email = instance.email
            send_mail(
                "Password Reset",
                f"Your new password is: {random_password}",
                "markopraksa@gmail.com",
                [email],
                fail_silently=False,
            )
            serializer.validated_data['password'] = random_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)