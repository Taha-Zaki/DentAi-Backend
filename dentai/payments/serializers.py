from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            'id', 'appointment', 'patient_name',
            'date', 'treatment_type',
            'total_amount', 'paid_amount', 'is_paid',
            'payment_method', 'tracking_code'
        ]
        read_only_fields = ['date', 'treatment_type', 'patient_name']

    def get_patient_name(self, obj):
        return obj.appointment.patient.user.get_full_name()
