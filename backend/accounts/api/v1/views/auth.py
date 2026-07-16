from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema

from accounts.api.v1.serializers.auth import SendOTPSerializer
from accounts.services.otp import OTPService
from accounts.services.sms import send_bulk_sms
from accounts.api.v1.serializers.auth import VerifyOTPSerializer
from accounts.services.jwt import JWTService

User = get_user_model()

@extend_schema(
    auth=[],
    request=SendOTPSerializer,
    responses={200: None},
)
class SendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = SendOTPSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data["phone_number"]

        user, created = User.objects.get_or_create(
            phone_number=phone_number
        )

        otp = OTPService.create_or_update(user)

        send_bulk_sms(
            message_text=f"کد تایید شما: {otp}",
            mobiles=[phone_number],
        )

        return Response(
            {
                "message": "OTP sent successfully",
                "phone_number": phone_number,
                "otp": otp,
            },
            status=status.HTTP_200_OK,
        )

@extend_schema(
    auth=[],
    request=VerifyOTPSerializer,
)  
class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data["phone_number"]
        otp_code = serializer.validated_data["otp_code"]

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "User not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        is_verified = OTPService.verify(user, otp_code)

        if not is_verified:
            return Response(
                {
                    "message": "Invalid or expired OTP."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        

        tokens = JWTService.issue_tokens(user)

        return Response(
            {
                "message": "OTP verified successfully.",
                **tokens,
            },
            status=status.HTTP_200_OK,
        )