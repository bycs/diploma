from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group

from users.models import CustomGroup, CustomUser, Department, Position


class DepartmentAdmin(admin.ModelAdmin):
    model = Department


class PositionAdmin(admin.ModelAdmin):
    model = Position


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "full_name", "birthday", "is_verification")
    ordering = ("is_verification", "email")
    list_filter = ("is_verification", "department", "position", "role", "is_staff", "is_superuser")
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = ("role", "user_permissions")
    fieldsets = (
        (None, {"fields": ("username", "email")}),
        ("ФИО", {"fields": ("first_name", "middle_name", "last_name")}),
        ("Разрешения", {"fields": ("is_staff", "is_active", "is_verification")}),
        ("Работа", {"fields": ("position", "department")}),
        ("Личные данные", {"fields": ("phone", "birthday")}),
        ("Полномочия", {"fields": ("role", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "email")}),
        ("ФИО", {"fields": ("first_name", "middle_name", "last_name")}),
        ("Разрешения", {"fields": ("is_staff", "is_active", "is_verification")}),
        ("Работа", {"fields": ("position", "department")}),
        ("Личные данные", {"fields": ("phone", "birthday")}),
    )


class CustomGroupAdmin(GroupAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
