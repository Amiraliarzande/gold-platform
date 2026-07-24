from django.db import models


class CartItemModel(models.Model):
    cart = models.ForeignKey(
        "cart.CartModel",
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "shop.ProductModel",
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    quantity = models.PositiveIntegerField(default=1)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["cart", "product"],
                name="unique_cart_product",
            )
        ]

    def __str__(self):
        return f"{self.product} ({self.quantity})"