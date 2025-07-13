from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, unique=True)
    national_id   = models.CharField(max_length=10, blank=True, null=True)


class Patient(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)

    # ───── اطلاعات هویتی ─────
    birth_date   = models.DateField(null=True, blank=True)
    gender       = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')], blank=True)
    occupation   = models.CharField(max_length=100, blank=True)
    phone        = models.CharField(max_length=15, blank=True)        # موبایل
    landline     = models.CharField(max_length=15, blank=True)        # تلفن منزل
    address      = models.TextField(blank=True)

    relative_job             = models.CharField(max_length=100, blank=True)   # شغل پدر/مادر/همسر
    record_completion_date   = models.DateField(null=True, blank=True)
    record_number            = models.CharField(max_length=30,  blank=True)

    # ───── بیماری‌ها ─────
    has_diabetes          = models.BooleanField(default=False)
    has_heart_disease     = models.BooleanField(default=False)
    has_tonsil_issue      = models.BooleanField(default=False)
    has_blood_disease     = models.BooleanField(default=False)
    has_allergy           = models.BooleanField(default=False)
    has_lung_disease      = models.BooleanField(default=False)
    has_history_of_hospitalization = models.BooleanField(default=False)
    other_diseases        = models.TextField(blank=True)

    current_medications   = models.TextField(blank=True)
    relationship_with_patient = models.CharField(max_length=100, blank=True)

    # ───── رضایت‌نامه ─────
    treatment_consent = models.BooleanField(default=False)
    consent_date      = models.DateField(null=True, blank=True)

    # ───── بررسی بالینی ─────
    problem_list      = models.TextField(blank=True)
    treatment_plan    = models.TextField(blank=True)
    retention_plan    = models.CharField(max_length=200, blank=True)
    system_used       = models.CharField(max_length=100, blank=True)

    crowding          = models.CharField(max_length=50, blank=True)
    protrusion_lips   = models.CharField(max_length=50, blank=True)
    molars            = models.CharField(max_length=50, blank=True)
    bite              = models.CharField(max_length=50, blank=True)
    midline           = models.CharField(max_length=50, blank=True)
    gingival_show     = models.CharField(max_length=50, blank=True)
    shift             = models.CharField(max_length=50, blank=True)
    dual_bite         = models.CharField(max_length=50, blank=True)

    # ───── نمایش خوانا ─────
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.record_number or self.id}"
