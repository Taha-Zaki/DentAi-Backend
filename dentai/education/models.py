# education/models.py

from django.db import models

class EducationItem(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF File'),
        ('aparat', 'Aparat Link'),
    ]

    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    file = models.FileField(upload_to='education_pdfs/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
