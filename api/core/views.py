from django.shortcuts import render
from .serializers import (
    FaqSerializer,
    ArticleSerializer,
    InterviewHelpSerializer,
    JobFilterSerializer,
)
from employers.models import Job
from employers.serializers import JobSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import Faq, Article, InterviewHelp


# Create your views here.


class FaqView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class ArticleView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class InterviewHelpView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = InterviewHelp.objects.all()
    serializer_class = InterviewHelpSerializer


class JobSearchView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        serializer = JobFilterSerializer(data=self.request.query_params)

        if serializer.is_valid():
            industry = serializer.validated_data.get("industry")
            location = serializer.validated_data.get("location")

            if industry:
                queryset = queryset.filter(industry=industry)

            if location:
                queryset = queryset.filter(location=location)

        return queryset
