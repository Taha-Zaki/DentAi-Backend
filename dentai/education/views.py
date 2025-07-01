from django.shortcuts import render
from rest_framework import viewsets
from .models import EducationItem
from .serializers import EducationItemSerializer

class EducationItemViewSet(viewsets.ModelViewSet):
    queryset = EducationItem.objects.all()
    serializer_class = EducationItemSerializer
