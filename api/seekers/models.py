from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from django.contrib.gis.db.models import PointField
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from core.models import Skill

# from employers.models import Application

User = get_user_model()


def passport_filepath(self, filename):
    return f"passports/{self.id}/passport.pdf"


def cv_filepath(self, filename):
    return f"cvs/{self.id}/cv.pdf"


def visa_filepath(self, filename):
    return f"visas/{self.id}/visa.pdf"


def geocode_location(location):
    geoLocator = Nominatim(user_agent="api")
    location = geoLocator.geocode(location)
    if location:
        return Point(location.longitude, location.latitude)
    return None


class SeekerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="SeekerProfile",
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        max_length=50,
        blank=True,
        null=True,
        unique=True,
    )

    city = models.CharField(
        verbose_name=_("City"),
        max_length=50,
        blank=True,
        null=True,
    )

    state = models.CharField(
        verbose_name=_("State"),
        max_length=50,
        blank=True,
        null=True,
    )

    country = models.CharField(
        verbose_name=_("Country"),
        max_length=50,
        blank=True,
        null=True,
    )

    location = PointField(
        _("Location"),
        null=True,
        blank=True,
    )

    ethnicity = models.CharField(
        verbose_name=_("Ethnicity"),
        max_length=50,
        blank=True,
        null=True,
    )

    skills = models.ManyToManyField(
        Skill,
        verbose_name=_("Skills"),
        related_name="seeker_profiles",
        blank=True,
    )

    cv = models.FileField(
        upload_to=cv_filepath,
        blank=True,
        null=True,
    )

    passport = models.FileField(
        upload_to=passport_filepath,
        blank=True,
        null=True,
    )

    visa = models.FileField(
        upload_to=visa_filepath,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.city or self.state or self.country:
            location_parts = []

            if self.city:
                location_parts.append(self.city)
            if self.state:
                location_parts.append(self.state)
            if self.country:
                location_parts.append(self.country)

            location = ", ".join(location_parts)
            self.location = geocode_location(location)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Qualification(models.Model):
    seeker_profile = models.ForeignKey(
        SeekerProfile,
        on_delete=models.CASCADE,
        related_name="qualifications",
        default=None,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    body = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title}"


class Experience(models.Model):
    seeker_profile = models.ForeignKey(
        SeekerProfile,
        on_delete=models.CASCADE,
        related_name="experiences",
        default=None,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    body = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title}"
