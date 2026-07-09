from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    joining_date = models.DateField()

class Department(models.Model):
    name = models.CharField(max_length=100)