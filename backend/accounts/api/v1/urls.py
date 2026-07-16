from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.api.v1.views.auth import SendOTPView, VerifyOTPView

urlpatterns = [
    path(
        "auth/send-otp/",
        SendOTPView.as_view(),
        name="send-otp",
    ),
    path(
        "auth/verify-otp/",
        VerifyOTPView.as_view(),
        name="verify-otp",
    ),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),
]