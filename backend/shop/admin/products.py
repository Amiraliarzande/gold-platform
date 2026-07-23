from django.contrib import admin

from shop.models import ProductModel

from .product_image import ProductImageInline


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "user",
        "price",
        "stock",
        "status",
        "created_date",
    )

    list_filter = (
        "status",
        "created_date",
    )

    search_fields = (
        "title",
        "slug",
    )

    filter_horizontal = (
        "category",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    inlines = [
        ProductImageInline,
    ]

    ordering = (
        "-created_date",
    )