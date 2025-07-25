from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, StaffLoginView, RequestOTPView, VerifyOTPView, PatientSearchView, PhoneNumberExistsView


router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')

urlpatterns = [
    path('auth/login-staff/', StaffLoginView.as_view()),
    path('auth/request-otp/', RequestOTPView.as_view()),
    path('auth/verify-otp/', VerifyOTPView.as_view()),
    path('patients/search/', PatientSearchView.as_view(), name='patient-search'),
    path('check-phone/', PhoneNumberExistsView.as_view(), name='check-phone'),
    path('', include(router.urls)),
]
