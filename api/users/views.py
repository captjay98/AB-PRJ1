from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import (
    RegisterView,
    SocialLoginView,
)


from dj_rest_auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
)


from .serializers import (
    UserSerializer,
    CustomUserSerializer,
    CustomRegisterSerializer,
    CustomLoginSerializer,
    CustomPasswordResetSerializer,
    CustomPasswordResetConfirmSerializer,
    CustomPasswordChangeSerializer,
)

User = get_user_model()


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CheckAuthenticated(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        user = self.request.user
        if user.is_authenticated:
            return Response({"Authenticated": "User is Authenticated"})
        return Response({"NotAuthenticated": "User Not Authenticated"})


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({"success": "CSRF cookie Set"})


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CustomRegisterView(RegisterView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomRegisterSerializer

    def get_response_data(self, user):
        response_data = super().get_response_data(user)
        custom_data = CustomUserSerializer(user).data
        response_data.update(custom_data)
        return response_data


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CustomLoginView(LoginView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomLoginSerializer

    def get_response(self):
        response = super().get_response()

        # Add account_type to response data
        user = self.request.user
        custom_data = CustomUserSerializer(user).data
        response.data.update(custom_data)

        return response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    # callback_url = # CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client


class UserLogOutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"success": "logout Successful"})


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "email/password_reset.html"
    subject_template_name = "email/password_reset_subject.txt"
    serializer_class = CustomPasswordResetSerializer


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = CustomPasswordResetConfirmSerializer


class CustomPasswordChangeView(PasswordChangeView):
    serializer_class = CustomPasswordChangeSerializer


class UserView(APIView):
    def get(self, request):
        user = self.request.user
        user = User.objects.get(id=user.id)
        serializer = UserSerializer(user)

        return Response(serializer.data)
