from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number', 'birth_date', 'is_admin', 'is_active', 'picture')
    list_filter = ('email', 'username', 'birth_date', 'is_admin', 'is_active')
    search_fields = ('email', 'username')

