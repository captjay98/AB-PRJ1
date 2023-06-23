from django.urls import path
from .views import (
    SeekerProfilesView,
    SeekerProfileDetailsView,
    EmployerProfileView,
    JobsView,
    JobView,
    ApplicationsView,
    # ApplicationView,
)


urlpatterns = [
    path("profile", EmployerProfileView.as_view()),
    path("seekers", SeekerProfilesView.as_view()),
    path("seekers/<int:id>", SeekerProfileDetailsView.as_view()),
    path("jobs", JobsView.as_view()),
    path("jobs/<int:id>", JobView.as_view()),
    path("jobs/<int:id>/applications", ApplicationsView.as_view()),
    # path("jobs/applications/<int:id>", ApplicationView.as_view()),
]
