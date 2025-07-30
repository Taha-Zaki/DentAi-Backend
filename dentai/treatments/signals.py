# treatments/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import Treatment

@receiver(post_save, sender=Appointment)
def sync_treatment_with_appointment(sender, instance, created, **kwargs):
    if created:
        Treatment.objects.create(
            appointment=instance,
            treatment_type=instance.treatment_type,
            predicted_start_time = instance.predicted_start_time,
            date=instance.date,
            status=instance.status,
            doctor_note=instance.doctor_note
        )
    else:
        # بروزرسانی Treatment موجود
        try:
            treatment = Treatment.objects.get(appointment=instance)
            treatment.treatment_type = instance.treatment_type
            treatment.predicted_start_time = instance.predicted_start_time
            treatment.date = instance.date
            treatment.status = instance.status
            treatment.doctor_note = instance.doctor_note
            treatment.save()
        except Treatment.DoesNotExist:
            # اگر به دلایلی treatment نبوده، ایجاد کن
            Treatment.objects.create(
                appointment=instance,
                treatment_type=instance.treatment_type,
                predicted_start_time = instance.predicted_start_time,
                date=instance.date,
                status=instance.status,
                doctor_note=instance.doctor_note
            )
