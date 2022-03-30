from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'date', 'star_rating', 'comment')
    list_filter = ('client', 'product', 'date', 'star_rating', 'comment')
    search_fields = ('client', 'product', 'date', 'star_rating', 'comment')
