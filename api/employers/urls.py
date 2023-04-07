from django.urls import path, include
from .views import (
    SeekerProfilesView,
    EmployerProfileView,
    JobView,
)


urlpatterns = [
    path("seekers", SeekerProfilesView.as_view()),
    path("seekers/{id}", SeekerProfilesView.as_view()),
    path("profile", EmployerProfileView.as_view()),
    path("jobs", JobView.as_view()),
]
