from django.contrib import admin
from .models import SeekerProfile, Skill, Qualification, Experience
from django.contrib.auth.admin import UserAdmin

# Register your models her.


class SeekerProfileAdmin(UserAdmin):
    list_display = (
        "user",
        "phone_number",
        "city",
        "state",
        "country",
        "ethnicity",
        # "skills",
        "cv",
        "passport",
        "visa",
    )
    search_fields = (
        "user",
        "phone_number",
        "city",
        "state",
        "country",
        "ethnicity",
    )

    filter_horizontal = ()

    list_filter = (
        "state",
        "country",
        "ethnicity",
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = {
        "name",
    }


class QualificationAdmin(admin.ModelAdmin):
    list_display = {
        "title",
        "body",
    }


class RegisterAdmin(admin.ModelAdmin):
    list_display = {
        "title",
        "body",
    }


admin.site.register(SeekerProfile)
admin.site.register(Skill)
admin.site.register(Qualification)
admin.site.register(Experience)
