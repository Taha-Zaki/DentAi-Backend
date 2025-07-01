from django.shortcuts import render

from rest_framework import viewsets
from .models import MedicalFile
from .serializers import MedicalFileSerializer

class MedicalFileViewSet(viewsets.ModelViewSet):
    queryset = MedicalFile.objects.all()
    serializer_class = MedicalFileSerializer
