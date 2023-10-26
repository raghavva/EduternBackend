from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class RegDetails(models.Model):
    test = models.IntegerField()