from django.urls import path, include
from .views import (
    SeekerHomeView,
    SeekerProfileView,
    ApplicationsView,
)  # UpdateSeekerProfileView

urlpatterns = [
    path("", SeekerHomeView.as_view()),
    path("profile", SeekerProfileView.as_view()),
    path("application", ApplicationsView.as_view()),
    # path("profile/<pk:id>", SeekerProfileView.as_view()),
]
