from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'treatment_type', 'total_amount', 'paid_amount', 'method', 'status', 'tracking_code', 'date']
