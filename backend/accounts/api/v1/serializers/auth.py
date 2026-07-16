from rest_framework import serializers

from accounts.validators import validate_iranian_cellphone_number


class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11,
        validators=[validate_iranian_cellphone_number],
    )

class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11,
        validators=[validate_iranian_cellphone_number],
    )

    otp_code = serializers.RegexField(
        regex=r"^\d{4}$",
        error_messages={
            "invalid": "OTP code must be exactly 4 digits.",
        },
    )