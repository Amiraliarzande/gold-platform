from django.contrib import admin

from coupon.models import CouponUsageModel


@admin.register(CouponUsageModel)
class CouponUsageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "coupon",
        "user",
        "created_date",
    )

    list_select_related = (
        "coupon",
        "user",
    )

    autocomplete_fields = (
        "coupon",
        "user",
    )

    search_fields = (
        "coupon__code",
        "coupon__title",
        "user__phone_number",
    )

    list_filter = (
        "created_date",
        "coupon",
    )

    readonly_fields = (
        "created_date",
    )

    ordering = (
        "-created_date",
    )