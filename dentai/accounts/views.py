from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Patient, User
from .serializers import PatientSerializer, UserSerializer, PatientSearchSerializer,PatientMiniSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()  # ✅ درست

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

import random, string
from kavenegar import KavenegarAPI, APIException, HTTPException
from django.conf import settings


# لیست و پروفایل بیماران
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().select_related('user')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()

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
                "role": "receptionist",
                "isAuthenticated": True
            })
        return Response({"error": "اطلاعات ورود نامعتبر است."}, status=400)



class RequestOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        if not phone:
            return Response({"error": "شماره موبایل وارد نشده."}, status=400)

        try:
            user = User.objects.get(phone_number=phone, is_patient=True)
        except User.DoesNotExist:
            return Response({"error": "کاربر یافت نشد."}, status=404)

        otp_code ='1234'   # ''.join(random.choices(string.digits, k=4))

        request.session['otp'] = otp_code
        request.session['phone'] = phone
        request.session.set_expiry(300)  # تنظیم زمان اعتبار کد به ۵ دقیقه
        print("کد OTP:", otp_code)

        # try:
        #     api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        #     params = {
        #         'sender' : '2000660110',
        #         'receptor': phone,
        #         'token': otp_code,
        #         'template': 'OTP',
        #         'type': 'sms'  # یا voice برای تماس صوتی
        #     }
        #     api.verify_lookup(params)
        # except (APIException, HTTPException) as e:
        #     print("SMS Error:", str(e))
        #     return Response({"error": "خطا در ارسال پیامک"}, status=500)

        return Response({"message": "کد با موفقیت ارسال شد."})

class VerifyOTPView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        code = request.data.get('code')

        if not code or not phone:
            return Response({"error": "شماره موبایل یا کد وارد نشده."}, status=400)

        if code == request.session.get('otp') and phone == request.session.get('phone'):
            try:
                user = User.objects.get(phone_number=phone, is_patient=True)
            except User.DoesNotExist:
                return Response({"error": "کاربر یافت نشد."}, status=404)

            refresh = RefreshToken.for_user(user)
            return Response({
                "token": str(refresh.access_token),
                "role": "patient",
                "isAuthenticated": True
            })

        return Response({"error": "کد اشتباه است یا منقضی شده."}, status=400)
    
    
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
class PatientMiniDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        try:
            patient = Patient.objects.select_related("user").get(id=patient_id)
            serializer = PatientMiniSerializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "بیمار یافت نشد."}, status=404)



class CreateAdminUserView(APIView):
    def post(self, request):
        # کلید امنیتی ساده
        key = request.data.get("key")
        if key != "dsf54gd45sgd1gtrh4fg1b":
            return Response({"error": "Unauthorized"}, status=403)

        User = get_user_model()
        username = "Drmousavi"
        password = "456"
        email = "Drmousavi@gmail.com"

        user = User.objects.filter(username=username).first()

        if user:
            if not user.is_superuser:
                return Response({"error": "User exists but is not superuser."}, status=400)

            user.set_password(password)
            user.email = email  # اگر خواستی ایمیل رو هم آپدیت کنه
            user.save()
            return Response({"message": "Superuser password updated successfully."})
        else:
            User.objects.create_superuser(username=username, password=password, email=email)
            return Response({"message": "Superuser created successfully."})