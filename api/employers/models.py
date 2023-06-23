from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from django.db import models
from django.conf import settings
from django.utils import timezone
from seekers.models import SeekerProfile, Skill


def geocode_location(location):
    geoLocator = Nominatim(user_agent="api")
    location = geoLocator.geocode(location)
    if location:
        return Point(location.longitude, location.latitude)
    return None


class EmployerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="EmployerProfile",
        related_name="EmployerProfile",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Job(models.Model):
    JOB_STATUS = (
        ("open", "open"),
        ("closed", "closed"),
    )

    recruiter = models.ForeignKey(
        EmployerProfile,
        on_delete=models.DO_NOTHING,
        related_name="jobRecruiter",
    )

    title = models.CharField(
        verbose_name="Job title",
        max_length=255,
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Job description",
        max_length=555,
        blank=True,
        null=True,
    )

    required_skills = models.ManyToManyField(
        Skill,
        verbose_name=("Required Skills"),
        blank=True,
    )

    city = models.CharField(
        verbose_name="Location",
        max_length=55,
        blank=True,
        null=True,
    )

    location = PointField(
        verbose_name=("Location"),
        null=True,
        blank=True,
    )

    industry = models.CharField(
        verbose_name="Industry",
        max_length=155,
        blank=True,
        null=True,
    )

    date_posted = models.DateTimeField(
        default=timezone.now,
    )

    job_status = models.CharField(
        verbose_name=("job_status"),
        max_length=50,
        choices=JOB_STATUS,
        default="open",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.city:
            location = self.city
            self.location = geocode_location(location)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Application(models.Model):
    APPLICATION_STATUS = (
        ("Submitted", "Submitted"),
        ("Reviewing", "Reviewing"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    )

    applicant = models.ForeignKey(
        SeekerProfile,
        on_delete=models.DO_NOTHING,
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.DO_NOTHING,
    )

    application_status = models.CharField(
        verbose_name=("Application_status"),
        max_length=50,
        choices=APPLICATION_STATUS,
        default="Submitted",
        blank=True,
        null=True,
    )

    date_applied = models.DateTimeField(
        auto_now_add=True,
    )
