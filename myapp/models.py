from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    desc = models.CharField(max_length=255)
    address = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10)