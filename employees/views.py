from django.shortcuts import render
from .models import Employee


def home(request):
    employees=Employee.objects.all()

    return render(request, "employees/home.html",{
        "employees": employees
    })

def add_employee(request):
    return render(request,"employees/add_employee.html")