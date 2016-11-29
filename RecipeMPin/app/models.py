"""
Definition of models.
"""

from django.contrib.auth.models import User
from django.contrib.auth.models import models


# Create your models here.
class twostep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pin = models.IntegerField()