# # appointments/urls.py


from django.urls import path, include
from .views import AppointmentViewSet, BatchAppointmentAddView, AppointmentAddTimeView, AppointmentStatusUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('appointments/batch-add/', BatchAppointmentAddView.as_view(), name='batch-add-appointments'),
    path('appointments/<int:pk>/update-status/', AppointmentStatusUpdateView.as_view(), name='update-appointment-status'),
    path('appointments/<int:pk>/add-time/', AppointmentAddTimeView.as_view(), name='add-time-to-appointment'),
    path('', include(router.urls)),
]
