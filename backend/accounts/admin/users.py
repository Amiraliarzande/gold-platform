from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "id",
        "phone_number",
        "user_type",
        "is_phone_verified",
        "is_staff",
        "is_active",
        "created_date",
    )

    list_filter = (
        "user_type",
        "is_phone_verified",
        "is_staff",
        "is_active",
        "is_superuser",
        "groups",
    )

    search_fields = (
        "phone_number",
    )

    ordering = (
        "-created_date",
    )

    readonly_fields = (
        "created_date",
        "updated_date",
        "last_login",
    )

    fieldsets = (
        ("اطلاعات کاربر", {
            "fields": (
                "phone_number",
                "password",
            )
        }),
        ("وضعیت حساب", {
            "fields": (
                "user_type",
                "is_phone_verified",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
        ("دسترسی‌ها", {
            "fields": (
                "groups",
                "user_permissions",
            )
        }),
        ("تاریخ‌ها", {
            "fields": (
                "last_login",
                "created_date",
                "updated_date",
            )
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "user_type",
                    "is_phone_verified",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )