from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ReviewStatusType(models.IntegerChoices):
    pending = 1, "در انتظار تایید"
    approved = 2, "تایید شده"
    rejected = 3, "رد شده"


class ReviewModel(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    product = models.ForeignKey(
        "shop.ProductModel",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rate = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    status = models.PositiveSmallIntegerField(
        choices=ReviewStatusType.choices,
        default=ReviewStatusType.pending,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_user_product_review",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.product}"