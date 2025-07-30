# payments/urls.py

from django.urls import path
from .views import PaymentDetailView, PaymentUpdateView, PaymentsByPatientView, LatestPaymentNumber, LatestPaymentView


urlpatterns = [
    path('patient/<int:patient_id>/', PaymentsByPatientView.as_view(), name='payments-by-patient'),
    path('patient/<int:patient_id>/payments/<int:payment_number>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('patient/<int:patient_id>/payments/<int:payment_number>/edit/', PaymentUpdateView.as_view(), name='payment-edit'),
    path('patient/<int:patient_id>/latest-number/', LatestPaymentNumber.as_view(), name='latest-payment-number'),
    path('patient/<int:patient_id>/latest-payment/', LatestPaymentView.as_view(), name='latest-payment'),

]

