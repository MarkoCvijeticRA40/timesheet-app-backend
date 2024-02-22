from rest_framework import serializers
from  timesheet_app_backend.timesheet.model.project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'client_id', 'lead_id' , 'status']

