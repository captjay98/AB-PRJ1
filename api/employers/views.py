from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    SeekerProfileSerializer,
    EmployerProfileSerializer,
    JobSerializer,
)
from .models import EmployerProfile, Job
from seekers.models import SeekerProfile
from users.serializers import UserSerializer


class EmployerProfileView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        if user.is_employer:
            try:
                employerProfile = EmployerProfile.objects.get(user=user)
            except EmployerProfile.DoesNotExist:
                return Response({"error": "No Employee Profile Found"})
            employerProfile = EmployerProfileSerializer(employerProfile)
            return Response({"employer": employerProfile.data})
        else:
            return Response({"unauthorized": "Only Employers can access this page"})

    def put(self, request):
        user = request.user
        if user.is_employer:
            try:
                employer_profile = EmployerProfile.objects.get(user=user)
                serializer = EmployerProfileSerializer(
                    employer_profile, data=request.data
                )
                if serializer.is_valid():
                    user.first_name = request.data.get("first_name", user.first_name)
                    user.last_name = request.data.get("last_name", user.last_name)
                    user.username = request.data.get("username", user.username)
                    user.email = request.data.get("email", user.email)
                    user.save()
                    serializer.save()

                    return Response({"success": serializer.data})
                return Response(
                    {"error": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except EmployerProfile.DoesNotExist:
                return Response(
                    {"error": "Employer profile does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )


class SeekerProfilesView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        user = self.request.user
        if user.is_employer:
            if "id" in kwargs:
                id = kwargs["id"]
                try:
                    profile = SeekerProfile.objects.get(id=id)
                    serializer = SeekerProfileSerializer(profile)
                    return Response(serializer.data)
                except SeekerProfile.DoesNotExist:
                    return Response(status=404)
            else:
                profiles = SeekerProfile.objects.all()
                serializer = SeekerProfileSerializer(profiles, many=True)
                return Response(serializer.data)
        else:
            return Response({"unauthorized": "Only Employers can access this page"})


class JobView(APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_employer:
            if "id" in kwargs:
                try:
                    recruiter = EmployerProfile.objects.get(user=user)
                    job = Job.objects.filter(recruiter=recruiter, id=id)
                    serializer = JobSerializer(job)
                    return Response(serializer.data)
                except Job.DoesNotExist:
                    return Response({"error": "No jobs posted by User"})
            else:
                recruiter = EmployerProfile.objects.get(user=user)
                jobs = Job.objects.filter(recruiter=recruiter)
                serializer = JobSerializer(jobs, many=True)
                return Response(serializer.data)
