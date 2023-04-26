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
from allauth.account.adapter import get_adapter
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


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "account_type",
        ]


def account_type_validator(value):
    if value not in ["seeker", "employer"]:
        raise serializers.ValidationError("Invalid account type.")


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    account_type = serializers.CharField(
        write_only=True,
        required=True,
        validators=[account_type_validator],
    )  # class Meta:
    #     model = User
    #     fields = ["id",
    #               "email",
    #               "username",
    #               "first_name",
    #               "last_name",
    #               "account_type",]

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["first_name"] = self.validated_data.get("first_name", "")
        data_dict["last_name"] = self.validated_data.get("last_name", "")
        data_dict["account_type"] = self.validated_data.get("account_type", "")
        return data_dict

    def custom_signup(self, request, user):
        account_types = ["seeker", "employer"]
        account_type = self.validated_data["account_type"]
        user.account_type = account_type
        if account_type not in account_types:
            raise serializers.ValidationError(
                {"account_type": "Invalid account type."},
            )

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
                {"error": "an unknown error occured"},
            )
        return super().custom_signup(request, user)


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password", "account_type"]

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
