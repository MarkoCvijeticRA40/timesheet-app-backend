from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from timesheet_app_backend.timesheet.model.project import Project
from timesheet_app_backend.timesheet.page_number_pagination import CustomPageNumberPagination
from timesheet_app_backend.timesheet.serializer.project_serializer import ProjectSerializer

class ProjectGenericView(GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.request.query_params.get('first_letter')
        if filter_param:
            queryset = queryset.filter(name__istartswith=filter_param[0])
        search_term = self.request.query_params.get('search_input', '')
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        client_id = self.request.query_params.get('client_id')
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        pk = self.request.query_params.get('pk')
        if pk:
            queryset = queryset.filter(pk=pk)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        pk = kwargs.get('pk')
        if pk:
            instance = get_object_or_404(queryset, pk=pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        page = self.paginate_queryset(queryset)
        if page:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)