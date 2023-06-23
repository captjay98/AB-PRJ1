from rest_framework import serializers
from .models import EmployerProfile, Job, Application
from seekers.serializers import UserSerializer, SeekerProfileSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployerProfile
        fields = [
            "user",
        ]


class JobSerializer(serializers.ModelSerializer):
    recruiter = EmployerProfileSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            "recruiter",
            "id",
            "title",
            "description",
            "required_skills",
            "city",
            "location",
            "industry",
            "job_status",
            "date_posted",
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = SeekerProfileSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            "applicant",
            "job",
            "application_status",
            "date_applied",
        ]
