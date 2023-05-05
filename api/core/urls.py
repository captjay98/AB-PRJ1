from django.urls import path
from .views import (
    SkillView,
    FaqView,
    ArticleView,
    InterviewHelpView,
    JobSearchView,
)


urlpatterns = [
    path("skills", SkillView.as_view()),
    path("search", JobSearchView.as_view()),
    path("faqs", FaqView.as_view()),
    path("articles", ArticleView.as_view()),
    path("interviewhelp", InterviewHelpView.as_view()),
]
