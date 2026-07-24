from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CouponModel(models.Model):
    title = models.CharField(max_length=255)

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    discount_percent = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ]
    )

    max_discount_amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        null=True,
        blank=True,
    )

    minimum_order_amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        default=0,
    )

    usage_limit = models.PositiveIntegerField(
        default=1,
    )

    used_count = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.code