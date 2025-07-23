# payments/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import Payment

@receiver(post_save, sender=Appointment)
def create_payment_on_completion(sender, instance, **kwargs):
    if instance.status == 'completed':
        Payment.objects.get_or_create(appointment=instance)
