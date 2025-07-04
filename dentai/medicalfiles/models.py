# medicalfiles/models.py

from django.db import models
from accounts.models import Patient

class MedicalFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('xray', 'X-ray'),
        ('link', 'Link'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_files')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file = models.FileField(upload_to='medical_files/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.file_type}"
