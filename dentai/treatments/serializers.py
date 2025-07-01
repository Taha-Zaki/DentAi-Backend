from rest_framework import serializers
from .models import TreatmentRecord

class TreatmentRecordSerializer(serializers.ModelSerializer):
    appointment_id = serializers.CharField(source='appointment.id', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = TreatmentRecord
        fields = ['id', 'appointment_id', 'notes', 'created_at']
