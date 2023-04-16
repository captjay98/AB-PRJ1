from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # , re_path

# from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/employers/", include("employers.urls")),
    path("api/seekers/", include("seekers.urls")),
    path("api/core/", include("core.urls")),
]


# urlpatterns += [
#     re_path(r"^.*", TemplateView.as_view(template_name="index.html")),
# ]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT,
#     )
