from django.db import models


class OrderStatusType(models.IntegerChoices):
    pending = 1, "در انتظار پرداخت"
    paid = 2, "پرداخت شده"
    processing = 3, "در حال آماده‌سازی"
    shipped = 4, "ارسال شده"
    delivered = 5, "تحویل داده شده"
    canceled = 6, "لغو شده"


class OrderModel(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.PROTECT,
        related_name="orders",
    )

    coupon = models.ForeignKey(
        "coupon.CouponModel",
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )

    status = models.PositiveSmallIntegerField(
        choices=OrderStatusType.choices,
        default=OrderStatusType.pending,
    )

    total_price = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=0,
    )

    discount_amount = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=0,
    )

    payable_amount = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=0,
    )

    tracking_code = models.CharField(
        max_length=100,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    shipped_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    delivered_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"Order #{self.id}"