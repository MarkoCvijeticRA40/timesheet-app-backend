from django.db import models
from django.db.models import ExpressionWrapper, F
from rest_framework import fields

from timesheet_app_backend.timesheet.model.category import Category
from timesheet_app_backend.timesheet.model.client import Client
from timesheet_app_backend.timesheet.model.employee import Employee
from timesheet_app_backend.timesheet.model.project import Project

class Task(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    hours = models.IntegerField(null=False)
    overtime = models.IntegerField(blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    def __str__(self):
        return f"{self.client_id} - {self.project_id} - {self.description}"