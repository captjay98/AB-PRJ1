from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from django.contrib.auth.models import Group


# Register your models here.


class User_Admin(UserAdmin):
    list_display = (
        # "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "account_type",
        "is_seeker",
        "is_employer",
        "is_admin",
        # "is_staff",
        "date_joined",
        "last_login",
    )
    search_fields = (
        "id",
        "email",
        "username",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )

    filter_horizontal = ()

    list_filter = (
        "account_type",
        "is_admin",
    )
    fieldsets = (
        (
            "personal",
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "account_type",
                    "is_staff",
                    "is_admin",
                    "is_active",
                )
            },
        ),
        ("status", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, User_Admin)
admin.site.unregister(Group)
