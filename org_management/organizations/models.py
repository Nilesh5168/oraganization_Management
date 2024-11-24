from django.db import models
from django.contrib.auth.models import AbstractUser 

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomUser (AbstractUser ):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username