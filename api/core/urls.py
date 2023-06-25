from django.urls import path
from .views import (
    IntelligentSearch,
    JobView,
    ApplicationsView,
    SkillView,
    FaqView,
    ArticleView,
    InterviewHelpView,
    JobSearchView,
)


urlpatterns = [
    path("", IntelligentSearch.as_view()),
    path("job/<int:id>", JobView.as_view()),
    path("job/<int:job_id>/application", ApplicationsView.as_view()),
    path("skills", SkillView.as_view()),
    path("search", JobSearchView.as_view()),
    path("faqs", FaqView.as_view()),
    path("articles", ArticleView.as_view()),
    path("interviewhelp", InterviewHelpView.as_view()),
]
