from rest_framework import serializers
from timesheet_app_backend.timesheet.model.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'client_id', 'project_id', 'category_id', 'description', 'hours', 'overtime', 'employee_id', 'date']

    def validate(self, data):
        client_id = data.get('client_id')
        project_id = data.get('project_id')
        if client_id and project_id and client_id != project_id.client_id:
            raise serializers.ValidationError("client_id must match project_id.client_id")
        return data