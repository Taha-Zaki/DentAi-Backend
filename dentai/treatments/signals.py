# treatments/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import Treatment

@receiver(post_save, sender=Appointment)
def create_treatment_for_appointment(sender, instance, created, **kwargs):
    if created:
        Treatment.objects.create(
            appointment=instance,
            treatment_type=instance.treatment_type,
            date=instance.date,
            status=instance.status
        )
