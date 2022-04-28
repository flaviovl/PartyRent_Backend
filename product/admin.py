from django.contrib import admin

from product.models import Category, Product


class ProductsInline(admin.TabularInline):
    model = Product
    extra = 1

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("category", "name", "description", "is_active", "price")
    list_filter = ("category", "name", "description", "is_active", "price")
    search_fields = ("category", "name", "description", "is_active", "price")

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    search_fields = ("name", "slug")
    inlines = [ProductsInline]
