from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from django.contrib.auth import get_user_model
from .models import (
    Skill,
    SeekerProfile,
    Qualification,
    Experience,
)

User = get_user_model()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ["id", "title", "body"]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "body"]


class SeekerProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")
    skills = SkillSerializer(many=True, required=False, read_only=True)
    experiences = ExperienceSerializer(many=True, required=False, read_only=True)
    qualifications = QualificationSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = SeekerProfile
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "username",
            "email",
            "id",
            "phone_number",
            "city",
            "state",
            "country",
            "ethnicity",
            "skills",
            "cv",
            "passport",
            "visa",
            "experiences",
            "qualifications",
        ]


class ProfileItemDeleteSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()

    class Meta:
        fields = ["id"]
