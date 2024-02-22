from django.db import models
from timesheet_app_backend.timesheet.model.client import Client
from timesheet_app_backend.timesheet.model.enum.project_status import ProjectStatus
from timesheet_app_backend.timesheet.model.employee import Employee

class Project(models.Model):

    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(blank=True, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    lead_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=ProjectStatus.choices, null=False)

    def __str__(self):
        return self.name