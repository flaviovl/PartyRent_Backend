
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem, ShoppingCart
from .serializers import (
    CartItemDetailSerializer,
    CartItemSerializer,
    RegisterCartSerializer,
    ShoppingCartDetailSerializer,
    ShoppingCartSerializer,
)


class CartItemAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if pk is None:
            items_qs = CartItem.objects.all()
            serializer = CartItemSerializer(items_qs, many=True)
        else:
            items_qs = CartItem.objects.filter(cart=pk)
            serializer = CartItemDetailSerializer(items_qs, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingCartAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, format=None):
        if pk is None:
            carts_qs = ShoppingCart.objects.all()
            serializer = RegisterCartSerializer(carts_qs, many=True)
        else:
            # queryset = ShoppingCart.objects.filter(user=request.user).filter(pk=pk) 
            cart_qs = get_object_or_404(ShoppingCart, id=pk)
            serializer = ShoppingCartDetailSerializer(cart_qs)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = RegisterCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
