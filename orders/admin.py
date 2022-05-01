from django.contrib import admin
from users.models import User

from .models import RentalOrder

# from shoppingcart.models import ShoppingCart


class RentalOrderInline(admin.TabularInline):
    model = RentalOrder
    extra = 0

class UserInline(admin.TabularInline):
    model = User
    extra = 0


@admin.register(RentalOrder)
class RentalOrder(admin.ModelAdmin):
    list_display = ("id", "client", "cart", "rental_date", "return_date", "amount", "status")
    list_filter = ("client", "cart", "rental_date", "return_date", "status")
    search_fields = ("id", "client", "cart")
    # inlines = [ShoppingCartInline]
