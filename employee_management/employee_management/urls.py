"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from frontend.views import login_view, register_view, dashboard_view, change_password_page, profile_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('employees/', include('employees.urls')),
    
    path("login/", login_view),
    path("register/", register_view),
    path("dashboard/", dashboard_view),
    path("change-password/", change_password_page),
    path("profile/", profile_view),
    path("", login_view),
]
