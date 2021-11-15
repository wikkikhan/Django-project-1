from django.contrib.auth import authenticate, login, views
from django.http import request
from django.shortcuts import render

from pages.models import Doctor, Patient
from .forms import AdminSignUpForm, DoctorRegistrationForm, DoctorSignUpForm, DoctorLoginForm, LoginForm, PatientSignupForm
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Group,User


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def adminclick_view(request):
    return render(request, 'pages/adminclick.html')

def doctorclick_view(request):
    return render(request, 'pages/doctorclick.html')

def patientclick_view(request):
    return render(request, 'pages/patientclick.html')


def admin_signup_view(request):
    if request.method == 'POST':
        fm = AdminSignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            messages.success(request, 'Your Account Created Successfully !!')
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('/adminlogin/')
    else:
        fm = AdminSignUpForm()
    return render(request, 'pages/adminsignup.html', {'form':fm})



def doctor_signup_view(request):
    if request.method == 'POST':
        fm = DoctorSignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your Account Created Successfully !!')
        return HttpResponseRedirect('/doctorlogin/')
    else:
        fm = DoctorSignUpForm()
    return render(request, 'pages/doctorsignup.html', {'form':fm})



def patient_signup_view(request):
    if request.method == 'POST':
        fm = PatientSignupForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            # messages.success(request, 'Your Account Created Successfully !!')
        return HttpResponseRedirect('/patientlogin/')
    else:
        fm = PatientSignupForm()
    return render(request, 'pages/patientsignup.html', {'form':fm})



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def admin_login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None and 'ADMIN':
                    login(request, user)
                    # messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/admindashboard')
        else:
            fm = LoginForm()
        return render(request, 'pages/adminlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/admindashboard')


# Doctor Login
def doctor_login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = DoctorLoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/doctordashboard')
        else:
            fm = DoctorLoginForm()
        return render(request, 'pages/doctorlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/doctordashboard')


# Patient Login
def patient_login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/patientdashboard')
        else:
            fm = LoginForm()
        return render(request, 'pages/patientlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/patientdashboard')

# def afterlogin_view(request):
#     if is_admin(request.user):
#         return render(request, 'pages/admin-dashboard.html')
#     elif is_doctor(request.user):
#         return render(request, 'pages/doctor-dashboard.html')
#     elif is_patient(request):
#         return render(request, 'pages/patient-admin.html')

def admin_dashboard_view(request):
    return render(request, 'pages/admin-dashboard.html')

def doctor_dashboard_view(request):
    return render(request, 'pages/doctor-dashboard.html')

def patient_dashboard_view(request):
    return render(request, 'pages/patient-dashboard.html')


# Doctor Registration Form
def Doctor_Registration_Form(request):
    if request.method == 'POST':
        fm = DoctorRegistrationForm(request.POST)
        if fm.is_valid():
            doctorName = fm.cleaned_data['doc_name']
            qualification = fm.cleaned_data['Qualification']
            specialization = fm.cleaned_data['specialization']
            doctorMobile = fm.cleaned_data['doc_mobile']
            doctorEmail = fm.cleaned_data['doc_email']
            doctorAddress = fm.cleaned_data['doc_addrs']
            # pwd = fm.cleaned_data['password']
            reg = Patient(doc_name=doctorName, Qualification=qualification, specialization=specialization, doc_mobile=doctorMobile, doc_email=doctorEmail, doc_addrs=doctorAddress)
            fm = DoctorRegistrationForm()
            messages.success(request, 'Appointment Created Successfully !!!')
            reg.save()
    else:
        fm = DoctorRegistrationForm()
    return render(request, 'pages/Doctors.html', {'form':fm})


# Patient Registration Form
# def patient_Registration_Form(request):
#     if request.method == 'POST':
#         fm = PatientRegistrationForm(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             smptms = fm.cleaned_data['symptoms']
#             doct = fm.cleaned_data['doctor']
#             gndr = fm.cleaned_data['gender']
#             mb = fm.cleaned_data['mobile']
#             em = fm.cleaned_data['email']
#             adrs = fm.cleaned_data['address']
            # pwd = fm.cleaned_data['password']
    #         reg = Patient(name=nm, symptoms=smptms, doctor=doct, gender=gndr, mobile=mb, email=em, address=adrs)
    #         fm = PatientRegistrationForm()
    #         messages.success(request, 'Appointment Created Successfully !!!')
    #         reg.save()
    # else:
    #     fm = PatientRegistrationForm()
    # return render(request, 'pages/Doctors.html', {'form':fm})


