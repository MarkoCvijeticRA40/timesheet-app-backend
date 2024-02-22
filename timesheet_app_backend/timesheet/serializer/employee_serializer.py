from rest_framework import serializers
from timesheet_app_backend.timesheet.model.employee import  Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'username', 'email', 'hours_per_week', 'status', 'role', 'password']