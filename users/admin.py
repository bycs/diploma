from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "full_name", "birthday", "is_verification")
    ordering = ("is_verification", "email")
    fieldsets = (
        (None, {"fields": ("username", "email")}),
        (
            "ФИО",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                )
            },
        ),
        ("Разрешения", {"fields": ("is_staff", "is_active", "is_verification")}),
        ("Личные данные", {"fields": ("birthday",)}),
        ("Полномочия", {"fields": ("groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "email")}),
        (
            "ФИО",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                )
            },
        ),
        ("Разрешения", {"fields": ("is_staff", "is_active", "is_verification")}),
        ("Личные данные", {"fields": ("birthday",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
