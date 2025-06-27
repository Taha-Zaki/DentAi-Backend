from django.db import models
from accounts.models import Patient
class MedicalFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to="medical_files/")
    file_type = models.CharField(max_length=20, choices=[
        ("xray", "X-ray"),
        ("pdf", "PDF"),
        ("image", "Image")
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)
