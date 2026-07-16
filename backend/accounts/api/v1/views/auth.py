from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.api.v1.serializers.auth import SendOTPSerializer
from accounts.services.otp import OTPService
from accounts.services.sms import send_bulk_sms


User = get_user_model()


class SendOTPView(APIView):

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