from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()  # Custom user

class MyUserAdmin(UserAdmin):
    list_display = ["email", "role", "first_name", "last_name", "is_staff", "is_active"]
    list_filter = ["email", "role"]
    search_fields = ["email", "role"]
    ordering = ["email", "role"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":("role",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields":("role",)}),
    )

admin.site.register(User, MyUserAdmin)