from django.db import models
from accounts.models import Patient
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    predicted_duration = models.IntegerField(help_text="in minutes")
    actual_duration = models.IntegerField(blank=True, null=True)
    treatment_type = models.CharField(max_length=255)

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("waiting", "Waiting"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("absent", "Absent"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
