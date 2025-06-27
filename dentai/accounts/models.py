from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=10, blank=True, null=True)
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    allergies = models.TextField(blank=True)
    diseases = models.TextField(blank=True)
    notes = models.TextField(blank=True)
