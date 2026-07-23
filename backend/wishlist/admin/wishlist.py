from django.contrib import admin

from wishlist.models import WishlistModel


@admin.register(WishlistModel)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
        "created_date",
    )

    list_filter = (
        "created_date",
    )

    search_fields = (
        "user__phone_number",
        "product__title",
    )

    autocomplete_fields = (
        "user",
        "product",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    ordering = (
        "-created_date",
    )