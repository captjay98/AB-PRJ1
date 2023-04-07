from django.urls import path, include
from .views import GetCSRFToken, UserRegistrationView, LoginView, LogOutView

urlpatterns = [
    path("getcsrf", GetCSRFToken.as_view()),
    path("register", UserRegistrationView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogOutView.as_view()),
]
