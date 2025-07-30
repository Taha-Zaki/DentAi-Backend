# treatments/serializers.py

from rest_framework import serializers
from .models import Treatment

class TreatmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    predicted_start_time = serializers.TimeField(format='%H:%M:%S')
    class Meta:
        model = Treatment
        fields = ['id', 'appointment', 'patient_name', 'treatment_type', 'predicted_start_time','status', 'date', 'doctor_note']

    def get_patient_name(self, obj):
        return obj.appointment.patient.user.get_full_name()
