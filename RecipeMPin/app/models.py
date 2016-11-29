"""
Definition of models.
"""

from django.db import models


# Create your models here.
class User(models.Model):
    identity = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    pin = models.IntegerField()


