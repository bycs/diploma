from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser, Role, RoleUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "fullname"]


class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = ["role_name"]
    search_fields = ["role_name"]


class RoleUserAdmin(admin.ModelAdmin):
    model = RoleUser
    list_display = ["user_id", "role_id"]
    list_filter = ["role_id"]
    search_fields = ["user_id", "role_id"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Role, RoleAdmin)
admin.site.register(RoleUser, RoleUserAdmin)
