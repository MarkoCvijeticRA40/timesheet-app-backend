from django.db import models

class Client(models.Model):

    name = models.CharField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.name}"

    #return f"{self.id}, {self.name}, {self.city}"