from django.conf import settings
from django.db import models

class PhoneVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="phone_verification",
    )

    otp_code = models.CharField(
        max_length=4,
        blank=True,
        default="",
    )

    is_used = models.BooleanField(default=False)

    otp_created_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Verification ({self.user.phone_number})"