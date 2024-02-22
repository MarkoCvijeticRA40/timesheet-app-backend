from django.db import models

class EmployeeRole(models.TextChoices):

    ADMIN = 'Admin', 'Admin'
    WORKER = 'Worker', 'Worker'