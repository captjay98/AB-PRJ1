from django.db import models
from django.db.models.fields import related
from django.conf import settings
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


ETHCHOICES = (
    ("Ethnicity", "Ethnicity"),
    ("African", "African"),
    ("African American", "African American"),
    ("Arab", "Arab"),
    ("Asian", "Asian"),
    ("Any other Asian background", "Any other Asian background"),
    ("Bangladeshi", "Bangladeshi"),
    ("Caribbean", "Caribbean"),
    ("Chinese", "Chinese"),
    ("English", "English"),
    ("Gypsy or Irish Traveller", "Gypsy or Irish Traveller"),
    ("Hispanic", "Hispanic"),
    ("Indian", "Indian"),
    ("Irish", "Irish"),
    ("Mixed or Multiple background", "Mixed or Multiple background"),
    ("Mixed or Multiple ethnic groups", "Mixed or Multiple ethnic groups"),
    ("Native American", "Native American"),
    ("Northern Irish", "Northern Irish"),
    ("Pacific Islander", "Pacific Islander"),
    ("Pakistani", "Pakistani"),
    ("Scottish", "Scotish"),
    ("White", "White"),
    ("White and Black African", "White and Black African"),
    ("White and Black Caribbean", "White and Black Caribbean"),
    ("Welsh", "Welsh"),
)


def passport_filepath(self, filename):
    return f"passports/{self.id}/passport.pdf"


def cv_filepath(self, filename):
    return f"cvs/{self.id}/cv.pdf"


def visa_filepath(self, filename):
    return f"visas/{self.id}/visa.pdf"


class Skill(models.Model):
    name = models.CharField(
        verbose_name=_("skill"),
        max_length=55,
    )

    def __str__(self):
        return f"{self.name}"


class SeekerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="SeekerProfile",
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
        verbose_name=_("State "),
        max_length=50,
        blank=True,
        null=True,
    )

    country = CountryField(
        verbose_name=_("Country"),
        max_length=50,
        blank=True,
        null=True,
    )

    ethnicity = models.CharField(
        verbose_name=_("Ethnicity"),
        max_length=50,
        choices=ETHCHOICES,
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
