from django.urls import include, path

from accounts.api.v1.views.auth import SendOTPView

urlpatterns = [
    path(
        "auth/send-otp/",
        SendOTPView.as_view(),
        name="send-otp",
    ),
]