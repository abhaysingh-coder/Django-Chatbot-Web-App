from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'role', 'is_staff')
    search_fields = ('email',)
    list_filter = ('role',)