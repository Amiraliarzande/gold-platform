from django.contrib import admin

from order.models import OrderItemModel


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product_title",
        "product",
        "price",
        "quantity",
        "created_date",
    )

    list_display_links = (
        "id",
        "product_title",
    )

    list_select_related = (
        "order",
        "product",
    )

    autocomplete_fields = (
        "order",
        "product",
    )

    search_fields = (
        "product_title",
        "product__title",
        "order__id",
    )

    list_filter = (
        "created_date",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    ordering = (
        "-created_date",
    )