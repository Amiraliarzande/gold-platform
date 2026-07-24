from django.contrib import admin

from cart.models import CartModel


@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "items_count",
        "created_date",
    )

    list_select_related = ("user",)

    search_fields = (
        "user__phone_number",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    ordering = ("-created_date",)

    def items_count(self, obj):
        return obj.items.count()

    items_count.short_description = "Items"