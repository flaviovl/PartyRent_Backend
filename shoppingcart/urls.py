from django.urls import path

from .views import CartItemAPIView, ShoppingCartAPIView

urlpatterns = [
    path("cartitem/", CartItemAPIView.as_view()),
    path("cartitem/<int:pk>", CartItemAPIView.as_view()),
    path("cart/", ShoppingCartAPIView.as_view()),
    path("cart/<int:pk>", ShoppingCartAPIView.as_view()),
    # path("cart/checkout/", checkout),
]
