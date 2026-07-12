from django.shortcuts import render,redirect 
from .models import Employee,Department
from django.db.models import Q
from django.contrib import messages


def home(request):

    search = request.GET.get("search")

    if search:

        employees = Employee.objects.filter(
            Q(employee_id__icontains=search) |
            Q(name__icontains=search) |
            Q(email__icontains=search)
            )

    else:

        employees=Employee.objects.all()

    return render(request, "employees/home.html",{
        "employees": employees,
        "search": search
    })

def add_employee(request):

    departments = Department.objects.all()

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = Department.objects.get(
            id=request.POST.get("department")
        )
        joining_date = request.POST.get("joining_date")
        photo = request.FILES.get("photo")
        
        employee = Employee(
        employee_id=employee_id,
        name=name,
        email=email,
        department=department,
        joining_date=joining_date,
        photo=photo,
    )
        
        employee.save()
        
        messages.success(request, "Employee added successfully.")
        

    return render(request, "employees/add_employee.html",{
        "departments": departments
    })

def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    departments = Department.objects.all()

    if request.method == "POST":

        employee.employee_id = request.POST.get("employee_id")
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.department = Department.objects.get(
            id=request.POST.get("department")
        )
        employee.joining_date = request.POST.get("joining_date")

        employee.save()

        messages.success(request, "Employee updated successfully.")


    return render(request, "employees/edit_employee.html",{
        "employee": employee,
        "departments": departments

    })

def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method != "POST":

        return render(request, "employees/delete_employee.html", {
            "employee": employee
        })

    employee.delete()

    messages.success(request, "Employee deleted successfully.")

    return redirect("home")

def department_list(request):

    departments = Department.objects.all()

    return render(request, "employees/department_list.html", {
        "departments": departments
    })

def add_department(request):

    if request.method == "POST":

        name = request.POST.get("name")

        department = Department(
            name=name
        )

        department.save()

        messages.success(request, "Department added successfully.")

    return render(request, "employees/add_department.html")

def edit_department(request, id):

    department = Department.objects.get(id=id)

    if request.method == "POST":

        department.name = request.POST.get("name")

        department.save()

        messages.success(request, "Department updated successfully.")

    return render(request, "employees/edit_department.html",{
        "department": department
    })
    
def delete_department(request, id):

    department = Department.objects.get(id=id)

    if request.method != "POST":

        return render(request, "employees/delete_department.html", {
            "department": department
        })

    department.delete()

    messages.success(request, "Department deleted successfully.")

    return redirect("department_list")