# payments/serializers.py

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    treatment_type = serializers.CharField(source='appointment.treatment_type', read_only=True)
    date = serializers.DateField(source='appointment.date', read_only=True)
    payment_number = serializers.IntegerField(read_only=True)  # نمایش شماره

    class Meta:
        model = Payment
        fields = [
            'id', 'appointment', 'payment_number',
            'patient_name', 'date', 'treatment_type',
            'total_amount', 'paid_amount', 'is_paid',
            'payment_method', 'tracking_code'
        ]

    def get_patient_name(self, obj):
        return obj.appointment.patient.user.get_full_name()
