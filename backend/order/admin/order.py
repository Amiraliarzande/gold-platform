from django.contrib import admin

from order.models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "status",
        "total_price",
        "discount_amount",
        "payable_amount",
        "coupon",
        "tracking_code",
        "created_date",
    )

    list_display_links = (
        "id",
        "user",
    )

    list_filter = (
        "status",
        "created_date",
        "paid_at",
        "shipped_at",
        "delivered_at",
    )

    search_fields = (
        "id",
        "user__phone_number",
        "tracking_code",
        "coupon__code",
    )

    autocomplete_fields = (
        "user",
        "coupon",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    ordering = (
        "-created_date",
    )

    fieldsets = (
        (
            "Order Information",
            {
                "fields": (
                    "user",
                    "status",
                    "coupon",
                ),
            },
        ),
        (
            "Payment",
            {
                "fields": (
                    "total_price",
                    "discount_amount",
                    "payable_amount",
                ),
            },
        ),
        (
            "Shipping",
            {
                "fields": (
                    "tracking_code",
                    "paid_at",
                    "shipped_at",
                    "delivered_at",
                ),
            },
        ),
        (
            "Description",
            {
                "fields": (
                    "description",
                ),
            },
        ),
        (
            "Dates",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_date",
                    "updated_date",
                ),
            },
        ),
    )