from rest_framework import serializers
from .models import EmployerProfile, Job
from seekers.models import SeekerProfile


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
