from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializers import PaymentSerializer
from appointments.models import Appointment

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('appointment__patient__user')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    search_fields = [
        'appointment__patient__user__first_name',
        'appointment__patient__user__last_name',
        'appointment__patient__user__username',
        'appointment__patient__user__phone_number',
    ]
    filterset_fields = ['appointment__patient__id']

    def create(self, request, *args, **kwargs):
        appointment_id = request.data.get('appointment')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found.'}, status=status.HTTP_400_BAD_REQUEST)

        # بررسی عدم وجود پرداخت قبلی
        if hasattr(appointment, 'payment'):
            return Response({'error': 'Payment already exists for this appointment.'}, status=400)

        payment = Payment.objects.create(
            appointment=appointment,
            date=appointment.date,
            treatment_type=appointment.treatment_type
        )
        serializer = self.get_serializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # ابتدا آپدیت فیلدها
        self.perform_update(serializer)

        # سپس بررسی تطابق پرداخت کامل
        instance.refresh_from_db()
        if instance.total_amount is not None and instance.paid_amount is not None:
            instance.is_paid = instance.total_amount == instance.paid_amount
            instance.save()

        return Response(self.get_serializer(instance).data)
