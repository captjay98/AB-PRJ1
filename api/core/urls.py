from django.urls import path
from .views import (
    FaqView,
    ArticleView,
    InterviewHelpView,
)


urlpatterns = [
    path("faqs", FaqView.as_view()),
    path("articles", ArticleView.as_view()),
    path("interviewhelp", InterviewHelpView.as_view()),
]
