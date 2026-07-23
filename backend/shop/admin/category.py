from django.contrib import admin

from shop.models import ProductCategoryModel


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "created_date",
    )

    search_fields = (
        "title",
        "slug",
    )

    ordering = (
        "-created_date",
    )