from django.db import models


class CouponUsageModel(models.Model):
    coupon = models.ForeignKey(
        "coupon.CouponModel",
        on_delete=models.CASCADE,
        related_name="usages",
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="coupon_usages",
    )

    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["coupon", "user"],
                name="unique_coupon_user",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.coupon.code}"