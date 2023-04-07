from django.contrib import admin
from .models import SeekerProfile, Skill, Qualification, Experience
from django.contrib.auth.admin import UserAdmin

# Register your models her.


class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "city",
        "state",
        "country",
        "ethnicity",
        # "skills",
        # "cv",
        # "passport",
        # "visa",
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

    list_filter = [
        "state",
        "country",
        "ethnicity",
    ]


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class QualificationAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
    ]


class RegisterAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
    ]


admin.site.register(SeekerProfile, SeekerProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Experience, RegisterAdmin)
