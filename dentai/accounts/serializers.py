from rest_framework import serializers
from .models import User, Patient

# Serializer برای ثبت یا مشاهده اطلاعات بیمار
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'national_id']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = [
            "id",
            "user",
            "birth_date",
            "gender",
            "occupation",
            "landline",
            "phone",
            "address",
            "relative_job",
            "record_completion_date",
            "record_number",

            # بیماری‌ها
            "has_diabetes",
            "has_heart_disease",
            "has_tonsil_issue",
            "has_blood_disease",
            "has_allergy",
            "has_lung_disease",
            "has_history_of_hospitalization",
            "other_diseases",

            "current_medications",
            "relationship_with_patient",

            # رضایت
            "treatment_consent",
            "consent_date",

            # کلینیکال
            "problem_list",
            "treatment_plan",
            "retention_plan",
            "system_used",
            "crowding",
            "protrusion_lips",
            "molars",
            "bite",
            "midline",
            "gingival_show",
            "shift",
            "dual_bite",
        ]

    # ‼️ اگر هنوز نیاز داری از متد create / update سفارشی استفاده شود:
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data, is_patient=True)
        return Patient.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            for attr, val in user_data.items():
                setattr(instance.user, attr, val)
            instance.user.save()

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance
    
    
class PatientSearchSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
