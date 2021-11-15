from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from .models import Doctor, DoctorSignup,Patient
from django.utils.translation import gettext_lazy as _


#Admin SignupForm
class AdminSignUpForm(UserCreationForm):
    password1 = forms.CharField(widget = PasswordInput(attrs = {'class':'form-control','placeholder':'Enter Password..'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'re-enter Password..'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # labels = {'first_name':'First Name', 'last_name':'Last Name','email': 'Email'}
        widgets = {
            'username' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Username..'}),
            'first_name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'first_name..'}), 
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name..'}), 
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email..'}),
            }



#Doctor SignupForm
class DoctorSignUpForm(forms.ModelForm):
    password1 = forms.CharField( label='Password', widget = PasswordInput(attrs = {'class':'form-control', 'placeholder':'Enter Password..'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'re-enter Password..'}))
    class Meta:
        model = DoctorSignup
        fields = ['name', 'address', 'mobile', 'department', 'status']
        # labels = {'first_name':'First Name', 'last_name':'Last Name','email': 'Email'}
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'name...'}),
            'address' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'address...'}), 
            'mobile' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'mobile...'}), 
            'department' : forms.TextInput({'class': 'form-control', 'placeholder':'deparment...'}),
            'status' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'status...'}),
            }

# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=models.Doctor
#         fields=['address','mobile','department','status','profile_pic']


#Patient SignupForm
class PatientSignupForm(forms.ModelForm):
    password1 = forms.CharField( label='Password', widget = PasswordInput(attrs = {'class':'form-control', 'placeholder':'Enter Password..'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'re-enter Password..'}))
    class Meta:
        model = Patient
        fields = ['name', 'symptoms', 'gender', 'mobile', 'email', 'address', 'doctor']
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Username..'}),
            'symptoms' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'symptoms..'}),
            'gender' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'gender..'}),
            'mobile' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'mobile..'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'email..'}),
            'address' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'address..'}),
            # 'doctor' : forms.ModelChoiceField(queryset=models.Doctor.objects.all(), empty_label=None, to_field_name="user_id"),
            # 'doctor' : forms.ModelChoiceField(queryset=doctor.object.all, empty_label=None ,attrs = {'class':'form-control'}),
            # 'password' : forms.PasswordInput(render_value=True, attrs = {'class': 'form-control'}),
        }


# Admin login class
class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'username...'}))
    password = forms.CharField(label= _("Password"), strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control', 'placeholder':'password...'}))

# Admin login class
class DoctorLoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'username...'}))
    password = forms.CharField(label= _("Password"), strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control', 'placeholder':'password...'}))


# class PatientRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['name', 'symptoms', 'gender', 'mobile', 'email', 'address', 'doctor']
#         widgets = {
#             'name' : forms.TextInput(attrs = {'class':'form-control'}),
#             'symptoms' : forms.TextInput(attrs = {'class':'form-control'}),
#             'gender' : forms.TextInput(attrs = {'class':'form-control'}),
#             'mobile' : forms.TextInput(attrs = {'class':'form-control'}),
#             'email' : forms.EmailInput(attrs = {'class': 'form-control'}),
#             'address' : forms.TextInput(attrs = {'class':'form-control'}),
            # 'doctor' : forms.ModelChoiceField(queryset=models.Doctor.objects.all(), empty_label=None, to_field_name="user_id"),
            # 'doctor' : forms.ModelChoiceField(queryset=doctor.object.all, empty_label=None ,attrs = {'class':'form-control'}),
            # 'password' : forms.PasswordInput(render_value=True, attrs = {'class': 'form-control'}),
        # }


class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name', 'Qualification', 'specialization', 'doc_mobile', 'doc_email', 'doc_addrs']
        widgets = {
            'doc_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'Qualification' : forms.TextInput(attrs = {'class':'form-control'}),
            'specialization' : forms.TextInput(attrs = {'class':'form-control'}),
            'doc_mobile' : forms.TextInput(attrs = {'class': 'form-control'}),
            'doc_email' : forms.EmailInput(attrs = {'class': 'form-control'}),
            'doc_addrs' : forms.Textarea(attrs = {'class':'form-control'}),
            # 'doctor' : forms.ModelChoiceField(queryset=doctor.object.all, empty_label=None ,attrs = {'class':'form-control'}),
            # 'password' : forms.PasswordInput(render_value=True, attrs = {'class': 'form-control'}),
        }
