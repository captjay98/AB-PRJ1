from rest_framework import serializers
from django.contrib.auth import get_user_model
from seekers.models import SeekerProfile
from employers.models import EmployerProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )
    re_password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Confirm Password"},
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "re_password",
            "account_type",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        re_password = validated_data.pop("re_password")
        account_type = validated_data["account_type"]
        if password != re_password:
            raise serializers.ValidationError(
                {"password": "Passwords must match."},
            )
        user = User(**validated_data)
        user.set_password(password)
        if account_type == "seeker":
            user.is_seeker = True
            user.save()
            seeker = SeekerProfile(user=user)
            seeker.save()
        elif account_type == "employer":
            user.is_employer = True
            user.save()
            employer = EmployerProfile(user=user)
            employer.save()
        else:
            raise serializers.ValidationError(
                {"account_type": "Invalid account type."},
            )
        return user


class UserLooginSerializer(serializers.ModelSerializer):
    pass
