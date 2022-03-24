from rest_framework import serializers
from .models import ShoppingCart, CartItem, RentalOrder


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class RentalOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalOrder
        fields = '__all__'
