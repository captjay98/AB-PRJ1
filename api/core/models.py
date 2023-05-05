from django.db import models


# Create your models here.


class Skill(models.Model):
    name = models.CharField(
        verbose_name=("skill"),
        max_length=55,
    )

    def __str__(self):
        return f"{self.name}"


class Faq(models.Model):
    question = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    answer = models.TextField(
        max_length=555,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.question


class Article(models.Model):
    tile = models.CharField(
        max_length=55,
        blank=True,
        null=True,
    )

    snippet = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    body = models.TextField(
        max_length=2255,
        blank=True,
        null=True,
    )

    author = models.TextField(
        max_length=2255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title} ny {self.author}"


class InterviewHelp(models.Model):
    tile = models.CharField(
        max_length=55,
        blank=True,
        null=True,
    )

    snippet = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    body = models.TextField(
        max_length=2255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
