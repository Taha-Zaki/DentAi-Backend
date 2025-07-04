from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import Payment

@receiver(post_save, sender=Appointment)
def create_payment_for_appointment(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'payment'):
            Payment.objects.create(
                appointment=instance,
                date=instance.date,
                treatment_type=instance.treatment_type
            )
