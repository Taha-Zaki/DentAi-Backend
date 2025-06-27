from django.db import models
from appointments.models import Appointment
class TreatmentRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
