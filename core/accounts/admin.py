from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    date_hierarchy = "created_date"
    list_display = ("email", "is_superuser", "is_active")
    search_fields = ("email",)
    ordering = ("created_date",)
    fieldsets = (
        ("احراز هویت", {"fields": ("email", "password")}),
        ("مجوزها", {"fields": ("is_superuser", "is_staff", "is_active")}),
        ("مجوزهای گروه", {"fields": ("groups", "user_permissions")}),
        ("تاریخ های مهم", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            "ایجاد کاربر جدید",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
