# treatments/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreatmentViewSet, LatestTreatmentView


router = DefaultRouter()
router.register('', TreatmentViewSet, basename='treatments')


urlpatterns = [
    path('latest/<int:patient_id>/', LatestTreatmentView.as_view(), name='latest-treatment'),
    path('', include(router.urls)),
]
