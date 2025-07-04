# medicalfiles/serializers.py

from rest_framework import serializers
from .models import MedicalFile

class MedicalFileSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = MedicalFile
        fields = ['id', 'patient', 'patient_name', 'file_type', 'file', 'url', 'description', 'created_at']

    def get_patient_name(self, obj):
        return obj.patient.user.get_full_name()
