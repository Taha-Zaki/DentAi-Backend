# treatments/models.py

from django.db import models
import datetime
from appointments.models import Appointment

class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='treatment')
    treatment_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    date = models.DateField()
    doctor_note = models.TextField(blank=True, null=True)
    predicted_start_time = models.TimeField(default=datetime.time(10, 0)) 

    def __str__(self):
        return f"{self.appointment.patient.user.get_full_name()} - {self.treatment_type} - {self.date}"
