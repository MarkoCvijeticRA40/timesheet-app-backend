from rest_framework import serializers
from timesheet_app_backend.timesheet.model.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'