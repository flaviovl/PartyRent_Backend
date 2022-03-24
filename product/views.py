from rest_framework import viewsets

from product.models import Product
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer