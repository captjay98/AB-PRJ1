from django.urls import path, include
from .views import (
    GetCSRFToken,
    UserRegistrationView,
    UserLoginView,
    UserLogOutView,
)

urlpatterns = [
    path("getcsrf", GetCSRFToken.as_view()),
    path("register", UserRegistrationView.as_view()),
    path("login", UserLoginView.as_view()),
    path("logout", UserLogOutView.as_view()),
]
