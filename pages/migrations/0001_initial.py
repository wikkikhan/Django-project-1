# Generated by Django 3.2.8 on 2021-11-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=70, verbose_name='Name')),
                ('Qualification', models.CharField(max_length=100, verbose_name='Qualification')),
                ('specialization', models.CharField(choices=[('Dermatologists', 'Dermatologists'), ('Cardiologist', 'Cardiologist'), ('Anesthesiologists', 'Anesthesiologists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Dermatologists', max_length=50)),
                ('doc_mobile', models.IntegerField(verbose_name='Mobile_No')),
                ('doc_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('doc_addrs', models.CharField(max_length=150, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('department', models.CharField(choices=[('Dermatologists', 'Dermatologists'), ('Cardiologist', 'Cardiologist'), ('Anesthesiologists', 'Anesthesiologists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Dermatologists', max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('symptoms', models.CharField(max_length=150, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.doctor')),
            ],
        ),
    ]
