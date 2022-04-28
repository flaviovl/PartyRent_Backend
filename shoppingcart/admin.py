from django.contrib import admin

from shoppingcart.models import CartItem, ShoppingCart


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    
@admin.register(ShoppingCart)
class ShoppingCart(admin.ModelAdmin):
    list_display = ("client", "status", "date_created")
    list_filter = ("client", "status", "date_created")
    search_fields = ("id", "client")
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "price", "quantity")
    list_filter = ("cart", "product", "price", "quantity")
    search_fields = ("id", "cart", "product")
