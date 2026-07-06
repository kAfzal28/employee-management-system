from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-employee/", views.add_employee, name="add_employee"),
    path("edit-employee/<int:id>/", views.edit_employee, name="edit_employee"),
]