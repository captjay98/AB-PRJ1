from django.urls import path, include
from .views import (
    EmployerHomeView,
    SeekerProfilesView,
    SeekerProfileDetailsView,
    EmployerProfileView,
    JobView,
)


urlpatterns = [
    path("home", EmployerHomeView.as_view()),
    path("profile", EmployerProfileView.as_view()),
    path("seekers", SeekerProfilesView.as_view()),
    path("seekers/<int:id>", SeekerProfileDetailsView.as_view()),
    path("jobs", JobView.as_view()),
    path("jobs/<int:id>", JobView.as_view()),
]
