from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    Skill,
    SeekerProfile,
    Qualification,
    Experience,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "account_type",
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ["id", "title", "body"]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "body"]


class SeekerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = SkillSerializer(many=True, required=False)
    qualifications = QualificationSerializer(many=True, required=False)
    experiences = ExperienceSerializer(many=True, required=False)

    class Meta:
        model = SeekerProfile
        fields = [
            "user",
            "id",
            "phone_number",
            "city",
            "state",
            "country",
            "location",
            "ethnicity",
            "skills",
            "cv",
            "passport",
            "visa",
            "experiences",
            "qualifications",
        ]

    def create(self, validated_data):
        qualifications_data = validated_data.pop("qualifications", [])
        experiences_data = validated_data.pop("experiences", [])
        skills_data = validated_data.pop("skills", [])

        seeker_profile = SeekerProfile.objects.create(**validated_data)

        for qualification_data in qualifications_data:
            Qualification.objects.create(
                seeker_profile=seeker_profile, **qualification_data
            )

        for experience_data in experiences_data:
            Experience.objects.create(
                seeker_profile=seeker_profile,
                **experience_data,
            )

        for skill_data in skills_data:
            skill = Skill.objects.get(name=skill_data["name"])
            seeker_profile.skills.add(skill)

        return seeker_profile

    def update(self, instance, validated_data):
        qualifications_data = validated_data.pop("qualifications", [])
        experiences_data = validated_data.pop("experiences", [])
        skills_data = validated_data.pop("skills", [])

        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("state", instance.state)
        instance.country = validated_data.get("country", instance.country)
        instance.ethnicity = validated_data.get(
            "ethnicity",
            instance.ethnicity,
        )
        instance.cv = validated_data.get("cv", instance.cv)
        instance.passport = validated_data.get("passport", instance.passport)
        instance.visa = validated_data.get("visa", instance.visa)
        instance.save()

        for qualification_data in qualifications_data:
            qualification_id = qualification_data.get("id")
            if qualification_id:
                qualification = Qualification.objects.get(
                    id=qualification_id, seeker_profile=instance
                )
                qualification.title = qualification_data.get(
                    "title", qualification.title
                )
                qualification.body = qualification_data.get(
                    "body",
                    qualification.body,
                )
                qualification.save()
            else:
                Qualification.objects.create(
                    seeker_profile=instance, **qualification_data
                )

        for experience_data in experiences_data:
            experience_id = experience_data.get("id")
            if experience_id:
                experience = Experience.objects.get(
                    id=experience_id, seeker_profile=instance
                )
                experience.title = experience_data.get(
                    "title",
                    experience.title,
                )
                experience.body = experience_data.get(
                    "body",
                    experience.body,
                )
                experience.save()
            else:
                Experience.objects.create(seeker_profile=instance, **experience_data)

        instance.skills.clear()
        for skill_data in skills_data:
            skill = Skill.objects.get(name=skill_data["name"])
            instance.skills.add(skill)

        return instance
