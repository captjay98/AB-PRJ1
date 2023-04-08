from django.urls import path, include
from .views import SeekerProfileView  # UpdateSeekerProfileView

urlpatterns = [
    path("profile", SeekerProfileView.as_view()),
    # path("update", UpdateSeekerProfileView.as_view()),
]
