from os import error

from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

# from employers.models import EmployerProfile
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# from seekers.models import SeekerProfile


from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
)


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({"success": "CSRF cookie Set"})


@method_decorator(ensure_csrf_cookie, name="dispatch")
class UserRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "user": serializer.data,
                        "success": "User Succesfully Created",
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except error:
            return Response({"error": "Something went wrong"})


# class LoginView(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         try:
#             data = self.request.data
#             email = data["email"]
#             password = data["password"]
#             user = authenticate(email=email.lower(), password=password)
#             if user:
#                 login(request, user)
#                 return Response({"success": "Login Succesful"})
#             else:
#                 return Response({"error": "Invalid Email or Password"})
#         except error:
#             return Response(
#                 {
#                     "error": "Something went wrong \
#                              while attempting Login, Please contact admin"
#                 }
#             )


@method_decorator(csrf_protect, name="dispatch")
class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response({"success": "Login successful"})


class UserLogOutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"success": "logout Successful"})
