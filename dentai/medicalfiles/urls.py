# medicalfiles/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalFileViewSet

router = DefaultRouter()
router.register('files', MedicalFileViewSet, basename='medicalfiles')

urlpatterns = [
    path('', include(router.urls)),
]
