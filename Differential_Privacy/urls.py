"""Differential_Privacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from pages import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('adminclick/', views.adminclick_view, name='adminclick'),
    path('doctorclick/', views.doctorclick_view, name='doctorclick'),
    path('patientclick/', views.patientclick_view, name='patientclick'),

    path('adminsignup/', views.admin_signup_view, name='adminsignup'),
    path('doctorsignup/', views.doctor_signup_view, name='doctorsignup'),
    path('patientsignup/', views.patient_signup_view, name='patientsignup'),

    # path('admin/', views.is_admin, name='admin'),

    path('adminlogin/', views.admin_login_view, name='adminlogin'),
    path('doctorlogin/', views.doctor_login_view, name='doctorlogin'),
    path('patientlogin/', views.patient_login_view, name='patientlogin'),

    # path('adminlogin/', LoginView.as_view(template_name='pages/adminlogin.html')),
    # path('doctorlogin/', LoginView.as_view(template_name='pages/doctorlogin.html')),
    # path('patientlogin/', LoginView.as_view(template_name = 'pages/patientlogin.html')),

    # path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='pages/index.html'), name='logout'),

    path('admindashboard/', views.admin_dashboard_view, name='admindashboard'),
    path('doctordashboard/', views.doctor_dashboard_view, name='doctordashboard'),
    path('patientdashboard/', views.patient_dashboard_view, name='patientdashboard'),
]
