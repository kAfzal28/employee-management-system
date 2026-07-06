from django.shortcuts import render,redirect 
from .models import Employee
from django.contrib import messages


def home(request):
    employees=Employee.objects.all()

    return render(request, "employees/home.html",{
        "employees": employees
    })

def add_employee(request):

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        joining_date = request.POST.get("joining_date")
        
        employee = Employee(
        employee_id=employee_id,
        name=name,
        email=email,
        department=department,
        joining_date=joining_date,
    )
        
        employee.save()
        
        messages.success(request, "Employee added successfully.")
        
        return redirect("add_employee")
        

    return render(request, "employees/add_employee.html")

def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.employee_id = request.POST.get("employee_id")
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.department = request.POST.get("department")
        employee.joining_date = request.POST.get("joining_date")

        employee.save()

        messages.success(request, "Employee updated successfully.")


    return render(request, "employees/edit_employee.html",{
        "employee": employee

    })