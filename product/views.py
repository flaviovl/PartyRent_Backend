from rest_framework import viewsets

from product.models import Product
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer