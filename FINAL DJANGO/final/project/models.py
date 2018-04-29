from django.db import models
from django.contrib.auth.models import User


class Ic(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    interviwer = models.ForeignKey(User, on_delete=models.CASCADE)