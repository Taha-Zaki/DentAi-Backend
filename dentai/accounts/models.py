# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=10, blank=True, null=True)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # اطلاعات پایه
    birth_date = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    place_of_birth = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'مذکر'), ('female', 'مونث')], blank=True)
    marital_status = models.CharField(max_length=10, choices=[('single', 'مجرد'), ('married', 'متاهل')], blank=True)
    education = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    landline = models.CharField(max_length=15, blank=True)

    # شرح حال و سوابق
    reason_for_visit = models.TextField(blank=True)
    under_doctor_observation = models.BooleanField(default=False)
    doctor_observation_reason = models.TextField(blank=True)

    # سوابق بیماری‌ها
    has_heart_disease = models.BooleanField(default=False)
    has_diabetes = models.BooleanField(default=False)
    has_lung_disease = models.BooleanField(default=False)
    has_respiratory_disease = models.BooleanField(default=False)
    has_allergy = models.BooleanField(default=False)
    has_autoimmune_disease = models.BooleanField(default=False)
    has_kidney_disease = models.BooleanField(default=False)
    has_bleeding_disorder = models.BooleanField(default=False)
    has_hepatitis = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    has_epilepsy = models.BooleanField(default=False)
    has_history_of_hospitalization = models.BooleanField(default=False)

    disease_description = models.TextField(blank=True)

    # مخصوص بانوان
    is_pregnant = models.BooleanField(default=False)
    is_in_menstrual_cycle = models.BooleanField(default=False)
    weeks_of_pregnancy = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.user.phone_number}"
