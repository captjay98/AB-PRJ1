from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import SeekerProfile, Qualification, Experience
from core.models import Skill
from .serializers import (
    SeekerProfileSerializer,
)
from employers.models import Application, Job
from employers.serializers import ApplicationSerializer

User = get_user_model()


class SeekerProfileView(APIView):
    def get(self, request):
        user = self.request.user
        if not user.is_seeker:
            return Response(
                {"error": "Seeker Only Page"},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            profile = SeekerProfile.objects.get(user=user)
        except SeekerProfile.DoesNotExist:
            return Response(
                {"error": "Profile Not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if profile.user != user:
            return Response(
                {"error": "You are not authorized to view this profile."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = SeekerProfileSerializer(profile)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, *args, **kwargs):
        user = self.request.user
        data = self.request.data

        if not user.is_seeker:
            return Response(
                {"error": "Seeker Only Page"},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            seeker_profile = SeekerProfile.objects.get(user=user)
            serializer = SeekerProfileSerializer(
                seeker_profile, data=data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except SeekerProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        if not user.is_seeker:
            return Response(
                {"error": "Seeker Only Page"},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            seeker_profile = SeekerProfile.objects.get(user=user)

            qualification_id = data.get("qualification_id")
            print("QUALIFICATION", qualification_id)
            if qualification_id:
                qualification = get_object_or_404(
                    Qualification,
                    id=qualification_id,
                    seeker_profile=seeker_profile,
                )
                qualification.delete()

            experience_id = data.get("experience_id")
            print("EXPERIENCE", experience_id)
            if experience_id:
                experience = get_object_or_404(
                    Experience,
                    id=experience_id,
                    seeker_profile=seeker_profile,
                )
                experience.delete()

            updated_user = SeekerProfile.objects.get(user=user)
            user_serializer = SeekerProfileSerializer(updated_user)

            return Response(
                user_serializer.data,
                status=status.HTTP_200_OK,
            )
        except SeekerProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ApplicationsView(APIView):
    def get(self, request):
        user = request.user
        applicant = SeekerProfile.objects.get(user=user)
        applications = Application.objects.filter(applicant=applicant)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     user = request.user
    #     data = request.data
    #     applicant = SeekerProfile.objects.get(user=user)
    #     job_id = data.get("job_id")
    #     job = Job.objects.get(id=job_id)

    #     serializer = ApplicationSerializer(data=data)
    #     if serializer.is_valid():
    #         application = serializer.save(
    #             applicant=applicant,
    #             job=job,
    #         )
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors,
    # status=status.HTTP_400_BAD_REQUEST)


# class SeekerProfileView(APIView):
#     def get(self, request):
#         user = self.request.user
#         if not user.is_seeker:
#             return Response(
#                 {"error": "Seeker Only Page"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         try:
#             profile = SeekerProfile.objects.get(user=user)
#         except SeekerProfile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         if profile.user != user:
#             return Response(
#                 {"error": "You are not authorized to view this profile."},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         serializer = SeekerProfileSerializer(profile)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK,
#         )

#     def put(self, request, *args, **kwargs):
#         user = self.request.user
#         if not user.is_seeker:
#             return Response(
#                 {"error": "Seeker Only Page"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         try:
#             seeker_profile = SeekerProfile.objects.get(user=user)
#         except SeekerProfile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         self._create_qualifications(request.data, seeker_profile)
#         self._create_experiences(request.data, seeker_profile)
#         self._add_skills(request.data, seeker_profile)

#         serializer = SeekerProfileSerializer(
#             seeker_profile, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#     def delete(self, request, *args, **kwargs):
#         user = self.request.user
#         data = self.request.data
#         if not user.is_seeker:
#             return Response(
#                 {"error": "Seeker Only Page"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )

#         try:
#             seekerprofile = SeekerProfile.objects.get(user=user)
#         except SeekerProfile.DoesNotExist:
#             return Response(
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         self._remove_skill(data, seekerprofile)
#         self._remove_qualification(data, seekerprofile)
#         self._remove_experience(data, seekerprofile)

#         serializer = SeekerProfileSerializer(seekerprofile)
#         return Response(
#             serializer.data,
#             status=status.HTTP_202_OK,
#         )

#     def _create_qualifications(self, data, seeker_profile):
#         if "qualifications" in data:
#             qualifications = data["qualifications"]
#             for q in qualifications:
#                 Qualification.objects.create(
#                     seeker_profile=seeker_profile,
#                     title=q["title"],
#                     body=q["body"],
#                 )

#     def _create_experiences(self, data, seeker_profile):
#         if "experiences" in data:
#             experiences = data["experiences"]
#             for e in experiences:
#                 Experience.objects.create(
#                     seeker_profile=seeker_profile,
#                     title=e["title"],
#                     body=e["body"],
#                 )

#     def _add_skills(self, data, seeker_profile):
#         if "skills" in data:
#             skills = data["skills"]
#             for s in skills:
#                 try:
#                     skill = Skill.objects.get(name=s["name"])
#                     seeker_profile.skills.add(skill)
#                 except Skill.DoesNotExist:
#                     return Response(
#                         {"error": "Skill does not exist"},
#                         status=status.HTTP_400_BAD_REQUEST,
#                     )

#     def _remove_qualification(self, data, seeker_profile):
#         if "qualification_id" in data:
#             qualification_id = data["qualification_id"]
#             try:
#                 qualification = Qualification.objects.get(
#                     id=qualification_id, seeker_profile=seeker_profile
#                 )
#                 qualification.delete()
#             except Qualification.DoesNotExist:
#                 return Response(
#                     {"error": "Qualification does not exist"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#     def _remove_experience(self, data, seeker_profile):
#         if "experience_id" in data:
#             experience_id = data["experience_id"]
#             try:
#                 experience = Experience.objects.get(
#                     id=experience_id, seeker_profile=seeker_profile
#                 )
#                 experience.delete()
#             except Experience.DoesNotExist:
#                 return Response(
#                     {"error": "Experience does not exist"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#     def _remove_skill(self, data, seekerprofile):
#         if "skill_id" in data:
#             skill_id = data["skill_id"]
#             try:
#                 skill = Skill.objects.get(id=skill_id)
#                 seekerprofile.skills.remove(skill)
#             except Skill.DoesNotExist:
#                 return Response(
#                     {"error": "Skill does not exist"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )


class SeekerHomeView(APIView):
    pass
