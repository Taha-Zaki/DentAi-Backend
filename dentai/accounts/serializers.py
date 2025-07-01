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
            'id',
            'user',
            'birth_date',
            'father_name',
            'place_of_birth',
            'gender',
            'marital_status',
            'education',
            'occupation',
            'address',
            'phone',
            'landline',
            'reason_for_visit',
            'under_doctor_observation',
            'doctor_observation_reason',
            'has_heart_disease',
            'has_diabetes',
            'has_lung_disease',
            'has_respiratory_disease',
            'has_allergy',
            'has_autoimmune_disease',
            'has_kidney_disease',
            'has_bleeding_disorder',
            'has_hepatitis',
            'is_smoker',
            'has_epilepsy',
            'has_history_of_hospitalization',
            'disease_description',
            'is_pregnant',
            'is_in_menstrual_cycle',
            'weeks_of_pregnancy'
        ]
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, is_patient=True)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance 

class PatientSearchSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
