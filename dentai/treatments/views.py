# treatments/views.py

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Treatment
from .serializers import TreatmentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.select_related('appointment__patient__user').order_by('id')
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['appointment__patient__id']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "درمان با موفقیت حذف شد."}, status=204)

class LatestTreatmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        latest = (
            Treatment.objects
            .filter(appointment__patient_id=patient_id)
            .select_related('appointment__patient__user')
            .order_by('-date', '-id')
            .first()
        )
        if not latest:
            return Response({"error": "درمانی برای این بیمار یافت نشد."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TreatmentSerializer(latest)
        return Response(serializer.data)
