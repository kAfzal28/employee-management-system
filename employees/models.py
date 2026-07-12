from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(
        "Department",
        on_delete=models.PROTECT
    )
    joining_date = models.DateField()
    photo = models.ImageField(
        upload_to="employee_photos/",
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name