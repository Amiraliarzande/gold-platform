from django.db import models


class OrderItemModel(models.Model):
    order = models.ForeignKey(
        "order.OrderModel",
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "shop.ProductModel",
        on_delete=models.PROTECT,
        related_name="order_items",
    )

    product_title = models.CharField(
        max_length=255,
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=0,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"],
                name="unique_order_product",
            )
        ]

    def __str__(self):
        return self.product_title