from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id", "email", "first_name", "last_name",
        "is_active", "is_staff", "is_superuser",
        "created_at", "updated_at"
    )
    list_display_links = ("id", "email")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "is_superuser")
    ordering = ("-created_at",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Shaxsiy ma'lumotlar", {
            "fields": ("first_name", "last_name", "avatar", "bio")
        }),
        ("Ruxsatlar", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Muhim vaqtlar", {
            "fields": ("last_login", "created_at", "updated_at")
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
