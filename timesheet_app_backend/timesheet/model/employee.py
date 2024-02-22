from django.db import models
from django.contrib.auth.models import AbstractUser
from timesheet_app_backend.timesheet.model.enum.employee_role import EmployeeRole
from timesheet_app_backend.timesheet.model.enum.employee_status import EmployeeStatus

class Employee(AbstractUser):

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    hours_per_week = models.IntegerField(null=False, default=0)
    status = models.CharField(max_length=255, choices=EmployeeStatus.choices, null=False)
    role = models.CharField(max_length=255, choices=EmployeeRole.choices, null=False)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
