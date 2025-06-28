from django.urls import path

from accounts.api_endpoints import (
    RegisterUserAPIView,
    RegisterConfirmAPIView,
    SessionLoginAPIView,
    SessionLogoutAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
    PasswordResetRequestAPIView,
    PasswordResetConfirmAPIView,
)
# from accounts.template_views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("register/confirm/", RegisterConfirmAPIView.as_view(), name="register-confirm"),
    path("login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("logout/", SessionLogoutAPIView.as_view(), name="logout-session"),

    path("profile/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    path("profile/delete/", ProfileDeleteAPIView.as_view(), name="profile-delete"),

    path("password-reset/request/", PasswordResetRequestAPIView.as_view(), name="password-reset"),
    path("password-reset/confirm/", PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
]

# template_urls = [
#     path("template/register/", RegisterView.as_view(), name="register-template"),
#     path("template/login/", LoginView.as_view(), name="login-template"),
#     path("template/profile/", ProfileView.as_view(), name="profile-template"),
# ]


