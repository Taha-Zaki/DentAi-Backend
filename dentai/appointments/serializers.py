# appointments/serializers.py

from rest_framework import serializers
from .models import Appointment
from accounts.models import Patient



class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.user.username', read_only=True)
    

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'treatment_type', 'predicted_start_time', 'predicted_duration', 'actual_start_time', 'actual_duration', 'status', 'date', 'doctor_note']



class BatchAppointmentInputSerializer(serializers.Serializer):
    date = serializers.DateField()
    start_time = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])
    appointments = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )

class AppointmentOutputSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = [
            "id", "patient", "patient_name", "treatment_type",
            "predicted_start_time", "predicted_duration",
            "actual_start_time", "actual_duration",
            "status", "date", 'doctor_note'
        ]

    def get_patient_name(self, obj):
        return obj.patient.user.first_name
    
    class AppointmentStatusUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Appointment
            fields = ['status']
