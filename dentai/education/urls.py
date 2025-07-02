# education/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationItemViewSet

router = DefaultRouter()
router.register(r'files', EducationItemViewSet, basename='education-files')

urlpatterns = [
    path('', include(router.urls)),
]
