from django.db import models


# Create your models here.
class User(models.Model):
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=20)
