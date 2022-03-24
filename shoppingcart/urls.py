from django.urls import include, path
from rest_framework import routers
from .views import ShoppingCartViewSet, CartItemViewSet, RentalOrderViewSet

router = routers.DefaultRouter()

router.register(r'cart', ShoppingCartViewSet)
router.register(r'cartitem', CartItemViewSet)
router.register(r'order', RentalOrderViewSet)

