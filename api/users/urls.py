from django.urls import path, include, re_path


from .views import (
    GetCSRFToken,
    CustomRegisterView,
    CustomLoginView,
    GoogleLogin,
    GithubLogin,
    CustomPasswordChangeView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
)

from dj_rest_auth.views import (
    LogoutView,
    # SocialLoginView,
    # SocialConnectView,
)

# from dj_rest_auth.registration.views import (
#     RegisterView,
#     VerifyEmailView,
#     ConfirmEmailView,
# )


urlpatterns = [
    # path("getcsrf", GetCSRFToken.as_view()),
    # path("account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
    path(
        "register",
        CustomRegisterView.as_view(),
        name="rest_register",
    ),
    path(
        "login",
        CustomLoginView.as_view(),
        name="rest_login",
    ),
    path(
        "logout",
        LogoutView.as_view(),
        name="rest_logout",
    ),
    path(
        "google/",
        GoogleLogin.as_view(),
        name="google_login",
    ),
    path(
        "github/",
        GithubLogin.as_view(),
        name="github_login",
    ),
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path(
        "password/change/",
        CustomPasswordChangeView.as_view(),
        name="rest_password_change",
    ),
    # path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    # path("registration/resend-email/", LogoutView.as_view()),
    # path(
    #     "account-confirm-email/",
    #     VerifyEmailView.as_view(),
    #     name="account_email_verification_sent",
    # ),
    # re_path(
    #     r"^account-confirm-email/(?P<key>[-:\w]+)/$",
    #     VerifyEmailView.as_view(),
    #     name="account_confirm_email",
    # ),
]
