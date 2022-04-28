from rest_framework import serializers
from users.serializers import UserMiniSerializer

from .models import CartItem, ShoppingCart


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="client.email")
    status = serializers.CharField(source="get_status_display")
    
    class Meta:
        model = ShoppingCart
        fields = "__all__"



# ================================================================================
class CartItemDetailSerializer(serializers.ModelSerializer):
    # product = ProductBasicSerializer()
    product = serializers.CharField(source="product.name")
    # sub_total = serializers.SerializerMethodField()   # total do item

    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "quantity",
            "price",
            "sub_total",
        )
        # depth = 1

    # def get_sub_total(self, instance):
    #     return instance.quantity * instance.price

class RegisterCartSerializer(serializers.ModelSerializer):
    # permission_classes = [permissions.IsAdminUser]            # somnente o admin pode listar todos os carrinhos
    client = serializers.CharField(source="client.email")
    products = CartItemDetailSerializer(many=True)
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = ShoppingCart
        fields = ["client", "status", "amount", "products"]

    def create(self, validated_data):
        products = validated_data.pop('products')
        cart = ShoppingCart.objects.create(**validated_data)
        for product in products:
            CartItem.objects.create(cart=cart, **product)
        return cart


class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    # cliente = serializers.SerializerMethodField()
    client = serializers.CharField(source='client.email')
    status = serializers.SerializerMethodField()
    products = CartItemDetailSerializer(many=True) # products é o related_name do model CartItem

    class Meta:
        model = ShoppingCart
        fields = (
            "id",
            "status",
            "client",
            "amount",
            "products",
            "date_created",
        )
        # depth = 1
    
    def get_cliente(self, instance):
        return {'id': instance.client.id, 'email': instance.client.email}

    def get_status(self, instance):
        return instance.get_status_display()
