# payments/models.py

from django.db import models
from appointments.models import Appointment

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    total_amount = models.PositiveIntegerField(default=0)
    paid_amount = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, blank=True)
    tracking_code = models.CharField(max_length=100, blank=True)
    
    payment_number = models.PositiveIntegerField()  # ← شماره‌ی محلی برای بیمار

    def save(self, *args, **kwargs):
        if not self.pk and not self.payment_number:
            patient = self.appointment.patient
            previous_payments = Payment.objects.filter(appointment__patient=patient).count()
            self.payment_number = previous_payments + 1

        self.is_paid = self.paid_amount >= self.total_amount    
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment #{self.payment_number} for {self.appointment}"
