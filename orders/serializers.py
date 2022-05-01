from rest_framework import serializers
from shoppingcart.serializers import ShoppingCartSerializer

from .models import RentalOrder


class RentalOrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentalOrder
        fields = (
            "id",
            "amount",
            "status",
        )
        depth = 0
        
        def get_status_display(self, obj):
            return obj.get_status_display()
        
class RentalOrderDetailSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="client.email")
    amount = serializers.FloatField(source="cart.amount")
    status = serializers.CharField(source="get_status_display")
    cart = ShoppingCartSerializer(many=False)

    class Meta:
        model = RentalOrder
        fields = (
            "id",
            "client",
            "rental_date",
            "return_date",
            "amount",
            "status",
            "cart",
        )
        depth = 0
        
        def get_status_display(self, obj):
            return obj.get_status_display()

