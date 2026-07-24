from django.contrib import admin

from cart.models import CartItemModel


@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
        "created_date",
    )

    list_select_related = (
        "cart",
        "cart__user",
        "product",
    )

    search_fields = (
        "cart__user__phone_number",
        "product__title",
    )

    list_filter = (
        "created_date",
    )

    autocomplete_fields = (
        "cart",
        "product",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    ordering = ("-created_date",)