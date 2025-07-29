from django.urls import path
from . import views

urlpatterns = [
    
    # Dynamic Forms
    path('forms/', views.dynamic_form_list_create),
    path('forms/<int:pk>/', views.dynamic_form_detail),

    # Employees
    path('employees/', views.employee_list_create),
    path('employees/<int:pk>/', views.employee_detail),
    
]