from django.urls import path, include
from .views import SeekerHomeView, SeekerProfileView  # UpdateSeekerProfileView

urlpatterns = [
    path("home", SeekerHomeView.as_view()),
    path("profile", SeekerProfileView.as_view()),
    # path("profile/<pk:id>", SeekerProfileView.as_view()),
]
