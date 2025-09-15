from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio',
                                        'is_online'
                                        )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
