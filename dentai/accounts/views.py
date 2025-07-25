from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Patient, User
from .serializers import PatientSerializer, UserSerializer, PatientSearchSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q



# لیست و پروفایل بیماران
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().select_related('user')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

# ورود منشی با username/password
class StaffLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_receptionist:
            refresh = RefreshToken.for_user(user)
            return Response({
                "token": str(refresh.access_token),
                "role": "receptionist"
            })
        return Response({"error": "اطلاعات ورود نامعتبر است."}, status=400)

# ورود بیمار با شماره موبایل و OTP (شبیه‌سازی‌شده)
class RequestOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        try:
            user = User.objects.get(phone_number=phone, is_patient=True)
            # اینجا به‌صورت واقعی باید کد ارسال شود
            request.session['otp'] = '1234'
            request.session['phone'] = phone
            return Response({"message": "کد ارسال شد."})
        except User.DoesNotExist:
            return Response({"error": "کاربر یافت نشد."}, status=404)

class VerifyOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        code = request.data.get('code')
        if code == request.session.get('otp') and phone == request.session.get('phone'):
            user = User.objects.get(phone_number=phone)
            refresh = RefreshToken.for_user(user)
            return Response({
                "token": str(refresh.access_token),
                "role": "patient"
            })
        return Response({"error": "کد اشتباه است."}, status=400)


class PatientSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query', '')
        patients = Patient.objects.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query) |
            Q(user__phone_number__icontains=query)
        )
        serializer = PatientSearchSerializer(patients, many=True)
        return Response(serializer.data)
class PhoneNumberExistsView(APIView):
    def get(self, request):
        phone = request.query_params.get('phone_number')
        if not phone:
            return Response({"error": "پارامتر phone_number الزامی است."}, status=400)
        
        exists = User.objects.filter(phone_number=phone).exists()
        return Response({
            "phone_number": phone,
            "exists": exists
        })
