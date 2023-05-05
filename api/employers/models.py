from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.utils import timezone

from seekers.models import SeekerProfile, Skill

# Create your models here.


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

    location = models.CharField(
        verbose_name="Location",
        max_length=55,
        blank=True,
        null=True,
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

    def __str__(self) -> str:
        return self.title


class Application(models.Model):
    APPLICATION_STATUS = (
        ("Submitted", "Submitted"),
        ("Reviewing", "Reviewing"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    )

    JOB_STATUS = (
        ("open", "open"),
        ("closed", "closed"),
    )

    applicant = models.ForeignKey(
        SeekerProfile,
        on_delete=models.DO_NOTHING,
    )

    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.DO_NOTHING,
    )

    job_status = models.CharField(
        verbose_name=("job_status"),
        max_length=50,
        choices=JOB_STATUS,
        blank=True,
        null=True,
    )

    application_status = models.CharField(
        verbose_name=("Application_status"),
        max_length=50,
        choices=APPLICATION_STATUS,
        blank=True,
        null=True,
    )

    date_applied = models.DateTimeField(
        auto_now_add=True,
    )

    # remars = moels.CharField("")
