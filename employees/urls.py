from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-employee/", views.add_employee, name="add_employee"),
    path("edit-employee/<int:id>/", views.edit_employee, name="edit_employee"),
    path("delete-employee/<int:id>/", views.delete_employee, name="delete_employee"),
    
    path("departments/", views.department_list, name="department_list"),
    path("add-department/", views.add_department, name="add_department"),
    path("edit-department/<int:id>/", views.edit_department, name="edit_department"),
    path("delete-department/<int:id>/", views.delete_department, name="delete_department"),
]