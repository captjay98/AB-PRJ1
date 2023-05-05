from rest_framework import serializers
from .models import EmployerProfile, Job, Application
from seekers.models import SeekerProfile, Experience, Qualification, Skill
from django_countries.serializers import CountryFieldMixin


class EmployerProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = EmployerProfile
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "username",
            "email",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["title", "body"]


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ["title", "body"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class SeekerProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    skills = SkillSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = SeekerProfile
        fields = [
            "id",
            "user",
            "phone_number",
            "city",
            "state",
            "country",
            "ethnicity",
            "skills",
            "cv",
            "passport",
            "visa",
            "experiences",
            "qualifications",
        ]


class JobSerializer(serializers.ModelSerializer):
    recruiter = serializers.PrimaryKeyRelatedField(read_only=True)
    # skills = SkillSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Job
        fields = [
            "recruiter",
            "id",
            "title",
            "description",
            "required_skills",
            "location",
            "industry",
            "date_posted",
        ]


class JobCreateSerializer(serializers.ModelSerializer):
    recruiter = serializers.PrimaryKeyRelatedField(read_only=True)
    # skills = SkillSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Job
        fields = [
            "recruiter",
            "id",
            "title",
            "description",
            "required_skills",
            "location",
            "industry",
            "date_posted",
        ]  # def create(self, **validated_data):


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        # fields = "__all__"
        fields = ["job_status", "application_status", "date_applied"]
