from rest_framework import serializers
from .models import Faq, Article, InterviewHelp
from employers.models import Job


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


class JobFilterSerializer(serializers.ModelSerializer):
    industries = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        help_text="Filter by industries.",
    )
    locations = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        help_text="Filter by locations.",
    )

    class Meta:
        model = Job
        fields = ["industries", "locations"]
