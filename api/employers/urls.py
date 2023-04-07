from django.urls import path, include
from .views import SeekerProfilesView, EmployerProfileView


urlpatterns = [
    # path("seekers", SeekerProfiles.as_view()),
    # path("seekers/{id}", SeekerProfiles.as_view()),
    path("profile", EmployerProfileView.as_view()),
    # path("jobs/{id}", JobView.as_view()),
]
