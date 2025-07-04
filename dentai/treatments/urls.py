# treatments/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreatmentViewSet

router = DefaultRouter()
router.register('', TreatmentViewSet, basename='treatments')

urlpatterns = [
    path('', include(router.urls)),
]
