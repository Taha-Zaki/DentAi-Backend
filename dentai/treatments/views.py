# treatments/views.py

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Treatment
from .serializers import TreatmentSerializer

class TreatmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Treatment.objects.select_related('appointment__patient__user').order_by('id')
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    
    search_fields = [
        'appointment__patient__user__first_name',
        'appointment__patient__user__last_name',
        'appointment__patient__user__username',
        'appointment__patient__user__phone_number',
    ]
    
    filterset_fields = [
        'appointment__patient__id',
        'status',
    ]
