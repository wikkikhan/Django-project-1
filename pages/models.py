from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Here is Doctor model
# class Doctor(models.Model):
#     doc_name = models.CharField(_('Name'), max_length=70)
#     Qualification = models.CharField(_('Qualification'), max_length=100)
#     specialization = models.CharField(_('Specialization'), max_length=100)
#     doc_mobile = models.IntegerField(_('Mobile_No'), )
#     doc_email = models.EmailField(_('Email'), max_length=100)
#     doc_addrs = models.CharField(_('Address'), max_length=150)

#     def __str__(self):
#         return self.doc_name
specialization = [
    ('Dermatologists','Dermatologists'),
    ('Cardiologist','Cardiologist'),
    ('Anesthesiologists','Anesthesiologists'),
    ('Allergists/Immunologists','Allergists/Immunologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
    ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
departments = [
    ('Dermatologists','Dermatologists'),
    ('Cardiologist','Cardiologist'),
    ('Anesthesiologists','Anesthesiologists'),
    ('Allergists/Immunologists','Allergists/Immunologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
    ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    doc_name = models.CharField(_('Name'), max_length=70)
    Qualification = models.CharField(_('Qualification'), max_length=100)
    # specialization = models.CharField(_('Specialization'), max_length=100)
    specialization = models.CharField(max_length=50, choices=specialization, default='Dermatologists')
    doc_mobile = models.IntegerField(_('Mobile_No'), )
    doc_email = models.EmailField(_('Email'), max_length=100)
    doc_addrs = models.CharField(_('Address'), max_length=150)

    def __str__(self):
        return self.doc_name
class DoctorSignup(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='Dermatologists')
    status = models.BooleanField(default=False)


# Here is Patient model
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=70)
    symptoms = models.CharField(max_length=150, null=True)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    # password = models.CharField(max_length=100)

    def __str__(self):
        return self.name