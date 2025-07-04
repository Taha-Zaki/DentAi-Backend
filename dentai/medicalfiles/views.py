# medicalfiles/views.py

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import MedicalFile
from .serializers import MedicalFileSerializer

class MedicalFileViewSet(viewsets.ModelViewSet):
    queryset = MedicalFile.objects.select_related('patient__user').all()
    serializer_class = MedicalFileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'patient__user__first_name',
        'patient__user__last_name',
        'patient__user__username',
        'patient__user__phone_number',
    ]
    filterset_fields = ['patient__id']
