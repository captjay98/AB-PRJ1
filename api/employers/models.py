from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.utils import timezone

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
    job_recruiter = models.ForeignKey(
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

    required_skills = models.TextField(
        verbose_name="Required Skills",
        max_length=255,
        blank=True,
        null=True,
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
