from django.shortcuts import render

from rest_framework import viewsets
from .models import TreatmentRecord
from .serializers import TreatmentRecordSerializer

class TreatmentRecordViewSet(viewsets.ModelViewSet):
    queryset = TreatmentRecord.objects.all()
    serializer_class = TreatmentRecordSerializer
