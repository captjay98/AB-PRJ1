from .serializers import (
    SkillSerializer,
    FaqSerializer,
    ArticleSerializer,
    InterviewHelpSerializer,
    JobFilterSerializer,
)


from seekers.models import SeekerProfile
from employers.models import Application
from employers.serializers import ApplicationSerializer
from rest_framework import status

# from seekers.models import SeekerProfile
from employers.models import Job
from employers.serializers import JobSerializer
from rest_framework import generics, permissions
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Faq, Article, InterviewHelp, Skill


class SkillView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


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


class HomeView(APIView):
    permission_classes = (permissions.AllowAny,)


class JobSearchView(generics.ListAPIView):
    def post(self, request, *args, **kwargs):
        pass

    # permission_classes = (permissions.AllowAny,)
    # serializer_class = JobSerializer

    # def get_queryset(self):
    #     queryset = Job.objects.all()
    #     serializer = JobFilterSerializer(data=self.request.query_params)

    #     if serializer.is_valid():
    #         industry = serializer.validated_data.get("industry")
    #         location = serializer.validated_data.get("location")
    #         skills = serializer.validated_data.get("skills")

    #         if industry:
    #             queryset = queryset.filter(industry=industry)

    #         if location:
    #             queryset = queryset.filter(location=location)

    #         if skills:
    #             queryset = queryset.filter(skills=skills)

    #     return queryset


def get_user_location(request):
    pass
    """get the current location of the
       user from the frontend in long and lat
    """


class IntelligentSearch(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        location = get_user_location(request)
        print(location)
        if location is not None:
            jobs = Job.objects.annotate(
                distance=Distance(
                    "location",
                    location,
                )
            ).filter(distance__lt=10000)
        else:
            jobs = Job.objects.all()

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        # user = request.user
        # seeker = SeekerProfile.objects.get(user=user)
        data = self.request.query_params
        serializer = JobFilterSerializer(data=data)

        if serializer.is_valid():
            industry = serializer.validated_data.get("industry")
            location = serializer.validated_data.get("location")
            skills = serializer.validated_data.get("skills")

        jobs = Job.objects.all()

        if location:
            location_point = Point(
                float(location.split(",")[1]), float(location.split(",")[0])
            )
            jobs = jobs.filter(
                location__distance_lte=(location_point, Distance(km=10)),
            )

        if industry:
            jobs = jobs.filter(industry__icontains=industry)

        if skills:
            jobs = jobs.filter(skills__icontains=skills)

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class JobView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        try:
            job = Job.objects.get(id=id)
            serializer = JobSerializer(job)
            return Response(
                serializer.data,
                status=200,
            )
        except Job.DoesNotExist:
            return Response(
                {"error": "Job Not Found"},
                status=404,
            )


class ApplicationsView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request):
        user = request.user
        applicant = SeekerProfile.objects.get(user=user)
        applications = Application.objects.filter(applicant=applicant)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # if "id" in kwargs:
        #    id = kwargs["id"]
        # job_id = kwargs.get("id")

        user = request.user
        data = request.data
        applicant = SeekerProfile.objects.get(user=user)
        id = kwargs["job_id"]
        job = Job.objects.get(id=id)

        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            application = serializer.save(
                applicant=applicant,
                job=job,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if industry and skills:
    #         results = Job.objects.filter(industry=industry,
    #                                       skills=skills,)
    #     elif industry:
    #         results = Job.objects.filter(industry=industry)
    #     elif location:
    #         results = Job.objects.filter(location=location)
    #     elif skills:
    #         results = Job.objects.filter(skills=skills)
    #     else:
    #         results = Job.objects.all()

    #     res = JobSerializer(data=results, many=True)

    # return Response(res.data)
