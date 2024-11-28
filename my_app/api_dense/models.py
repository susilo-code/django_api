from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.TextField()
    deptid = models.IntegerField()
    salary = models.IntegerField()