from rest_framework import serializers
from .models import MedicalFile

class MedicalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalFile
        fields = ['id', 'patient', 'file', 'file_type', 'uploaded_at']
