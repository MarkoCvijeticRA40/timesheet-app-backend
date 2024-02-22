from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=250, unique=True, null=False);

    def __str__(self):
        return self.name