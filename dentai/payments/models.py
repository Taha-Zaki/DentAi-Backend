from django.db import models
from accounts.models import Patient
class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=255)
    total_amount = models.PositiveIntegerField()
    paid_amount = models.PositiveIntegerField(default=0)
    method = models.CharField(max_length=50, choices=[
        ("cash", "Cash"),
        ("pos", "POS"),
        ("card", "Card"),
        ("online", "Online")
    ])
    tracking_code = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    @property
    def status(self):
        if self.paid_amount == 0:
            return "unpaid"
        elif self.paid_amount < self.total_amount:
            return "partial"
        return "paid"
