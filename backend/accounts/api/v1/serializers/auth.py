from rest_framework import serializers

from accounts.validators import validate_iranian_cellphone_number


class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11,
        validators=[validate_iranian_cellphone_number],
    )