from django.shortcuts import render
from .serializers import (
    FaqSerializer,
    ArticleSerializer,
    InterviewHelpSerializer,
)
from rest_framework import generics
from .models import Faq, Article, InterviewHelp


# Create your views here.


class FaqView(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class ArticleView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = FaqSerializer


class InterviewHelpView(generics.ListAPIView):
    queryset = InterviewHelp.objects.all()
    serializer_class = FaqSerializer
