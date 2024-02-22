from django.db import models

class EmployeeStatus(models.TextChoices):

    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'

