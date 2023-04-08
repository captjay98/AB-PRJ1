from rest_framework import serializers
from .models import Faq, Article, InterviewHelp


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ["__all__"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["__all__"]


class InterviewHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewHelp
        fields = ["__all__"]
