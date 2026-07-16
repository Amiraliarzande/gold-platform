import random

from django.utils import timezone
from datetime import timedelta

from accounts.models import PhoneVerification


class OTPService:

    @staticmethod
    def generate_otp():
        return str(random.randint(1000, 9999))

    @staticmethod
    def create_or_update(user):
        otp = OTPService.generate_otp()

        verification, created = PhoneVerification.objects.get_or_create(
            user=user
        )

        verification.otp_code = otp
        verification.is_used = False
        verification.otp_created_at = timezone.now()

        verification.save(
            update_fields=[
                "otp_code",
                "is_used",
                "otp_created_at",
            ]
        )

        return otp
    
    @staticmethod
    def verify(user, otp_code):
        verification = PhoneVerification.objects.get(user=user)

        if verification.otp_code != otp_code:
            return False

        if verification.is_used:
            return False

        if timezone.now() > verification.otp_created_at + timedelta(minutes=2):
            return False

        verification.is_used = True
        verification.save(update_fields=["is_used"])

        user.is_phone_verified = True
        user.save(update_fields=["is_phone_verified"])

        return True