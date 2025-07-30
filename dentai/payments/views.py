# payments/views.py

from rest_framework import generics
from rest_framework.views import APIView
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all().order_by("id")
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # یا AllowAny اگر عمومی می‌خوای
    
    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Payment.objects.filter(appointment__patient_id=patient_id).order_by('payment_number')

    def get_object(self):
        return self.get_queryset().get(payment_number=self.kwargs['payment_number'])

class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all().order_by("id")
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        print("=== UPDATE PAYMENT ===")
        print("METHOD:", request.method)
        print("DATA:", request.data)
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Payment.objects.filter(appointment__patient_id=patient_id).order_by('payment_number')

    def get_object(self):
        return self.get_queryset().get(payment_number=self.kwargs['payment_number'])

class PaymentsByPatientView(generics.ListAPIView):
    serializer_class = PaymentSerializer           
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Payment.objects.filter(appointment__patient_id=patient_id).order_by('payment_number')


class LatestPaymentNumber(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        latest = (
            Payment.objects
            .filter(appointment__patient_id=patient_id)
            .order_by('-payment_number')
            .first()
        )
        return Response({
            "patient_id": patient_id,
            "latest_payment_number": latest.payment_number if latest else 0
        })
    
class LatestPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        latest = (
            Payment.objects
            .filter(appointment__patient_id=patient_id)
            .select_related('appointment__patient__user')
            .order_by('-payment_number')
            .first()
        )
        if not latest:
            return Response({"error": "پرداختی یافت نشد."}, status=404)

        serializer = PaymentSerializer(latest)
        return Response(serializer.data)
