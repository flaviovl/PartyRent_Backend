
from rest_framework import viewsets

from .models import ShoppingCart, CartItem, RentalOrder
from .serializers import ShoppingCartSerializer, CartItemSerializer, RentalOrderSerializer
from rest_framework.permissions import IsAuthenticated



class ShoppingCartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class RentalOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = RentalOrder.objects.all()
    serializer_class = RentalOrderSerializer
