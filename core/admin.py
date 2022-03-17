from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaserUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaserUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","phone","email"),
            },
        ),
    )
