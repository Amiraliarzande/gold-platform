from django.contrib import admin

from review.models import ReviewModel


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "user",
        "rate",
        "status",
        "created_date",
    )

    list_filter = (
        "status",
        "rate",
        "created_date",
    )

    search_fields = (
        "title",
        "description",
        "user__phone_number",
        "product__title",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
    )

    autocomplete_fields = (
        "user",
        "product",
    )

    ordering = (
        "-created_date",
    )