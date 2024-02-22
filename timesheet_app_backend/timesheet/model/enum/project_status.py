from django.db import models

class ProjectStatus(models.TextChoices):

    ARCHIVE = 'Archive', 'Archive'
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'