from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from seekers.models import SeekerProfile
from employers.models import EmployerProfile
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import (
    RegisterSerializer,
    SocialLoginSerializer,
    SocialConnectSerializer,
)

from dj_rest_auth.serializers import (
    LoginSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    PasswordChangeSerializer,
)

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
            "account_type",
        ]


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
    )
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
    )
    password1 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    account_type = serializers.ChoiceField(
        choices=(("seeker", "seeker"), ("employer", "employer")), required=True
    )

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Passwords must match."},
            )

        return attrs

    def custom_signup(self, request, user):
        account_type = self.validated_data["account_type"]
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


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        if email and password:
            user = authenticate(email=email.lower(), password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        "User account is disabled.",
                    )
            else:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials."
                )
        else:
            raise serializers.ValidationError(
                'Must include "email" and "password".',
            )
        data["user"] = user
        return data


class CustomPasswordResetSerializer(PasswordResetSerializer):
    pass


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    pass


class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    pass


class GoogleLoginSerializer(SocialLoginSerializer):
    provider = "google"


class GoogleConnectSerializer(SocialConnectSerializer):
    provider = "google"


class GitHubLoginSerializer(SocialLoginSerializer):
    provider = "github"


class GitHubConnectSerializer(SocialConnectSerializer):
    provider = "github"
