from django.urls import path, include
from .views import (
    SeekerHomeView,
    SeekerProfileView,
    ApplicationsView,
)

urlpatterns = [
    path("", SeekerHomeView.as_view()),
    path("profile", SeekerProfileView.as_view()),
    path("application", ApplicationsView.as_view()),
    # path("jobs/<int:id>", JobsView.as_view()),
    path("job/<int:id>/application", ApplicationsView.as_view()),
]
