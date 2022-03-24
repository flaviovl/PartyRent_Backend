from django.urls import include, path
from rest_framework import routers
from product.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename="product",)
router.register(r'category', CategoryViewSet, basename="category",)
