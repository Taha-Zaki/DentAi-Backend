from django.db import models

class EducationItem(models.Model):
    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[
        ("video", "Video"),
        ("pdf", "PDF")
    ])
    file_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
