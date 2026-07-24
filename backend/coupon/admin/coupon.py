from django.contrib import admin

from coupon.models import CouponModel


@admin.register(CouponModel)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "code",
        "discount_percent",
        "minimum_order_amount",
        "usage_limit",
        "used_count",
        "is_active",
        "start_date",
        "end_date",
    )

    list_display_links = (
        "id",
        "title",
    )

    list_filter = (
        "is_active",
        "start_date",
        "end_date",
        "created_date",
    )

    search_fields = (
        "title",
        "code",
    )

    readonly_fields = (
        "used_count",
        "created_date",
        "updated_date",
    )

    ordering = (
        "-created_date",
    )

    fieldsets = (
        (
            "Coupon Information",
            {
                "fields": (
                    "title",
                    "code",
                    "is_active",
                ),
            },
        ),
        (
            "Discount",
            {
                "fields": (
                    "discount_percent",
                    "max_discount_amount",
                    "minimum_order_amount",
                ),
            },
        ),
        (
            "Usage",
            {
                "fields": (
                    "usage_limit",
                    "used_count",
                ),
            },
        ),
        (
            "Validity",
            {
                "fields": (
                    "start_date",
                    "end_date",
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