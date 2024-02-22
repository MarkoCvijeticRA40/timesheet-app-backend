from django.db import transaction
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from timesheet_app_backend.timesheet.model.task import Task
from timesheet_app_backend.timesheet.serializer.task_serializer import TaskSerializer

class TaskGenericView(GenericAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        date = request.query_params.get('date')
        if date:
            queryset = queryset.filter(date=date)
        queryset = queryset.order_by('-date')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        task_data_list = request.data
        updated_tasks = []
        try:
            for task_data in task_data_list:
                task_id = task_data.get('id')
                task_instance = Task.objects.get(pk=task_id)
                serializer = TaskSerializer(task_instance, data=task_data, partial=True)
                if serializer.is_valid():
                    if serializer.validated_data != task_instance.__dict__:
                        serializer.save()
                        updated_tasks.append(serializer.data)
                else:
                    raise Exception(serializer.errors)
        except Task.DoesNotExist:
            raise Exception({"error": "Task with this ID does not exist."})
        return Response(updated_tasks, status=status.HTTP_200_OK)