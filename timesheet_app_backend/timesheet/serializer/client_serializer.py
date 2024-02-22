from rest_framework import serializers
from timesheet_app_backend.timesheet.model.client import  Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'city', 'postal_code', 'country']