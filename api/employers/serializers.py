from rest_framework import serializers
from .models import EmployerProfile, Job
from seekers.models import SeekerProfile, Experience, Qualification
from django_countries.serializers import CountryFieldMixin


class EmployerProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = EmployerProfile
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["title", "body"]


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ["title", "body"]


class SeekerProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)

    class Meta:
        model = SeekerProfile
        fields = [
            "id",
            "user",
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


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "recruiter",
            "title",
            "description",
            "required_skills",
            "location",
            "industry",
            "date_posted",
        ]
