from django.db import models
from appointments.models import Appointment

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'نقدی'),
        ('card', 'کارت‌خوان'),
        ('online', 'آنلاین'),
        ('other', 'سایر'),
    ]

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    date = models.DateField()
    treatment_type = models.CharField(max_length=100)
    
    total_amount = models.PositiveIntegerField(null=True, blank=True)
    paid_amount = models.PositiveIntegerField(null=True, blank=True)
    
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)
    tracking_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.appointment.patient.user.get_full_name()} - {self.treatment_type} - {self.date}"
