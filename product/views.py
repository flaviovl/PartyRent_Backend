from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Category, Product
from product.serializers import (
    CategoryBasicSerializer,
    CategorySerializer,
    ProductBasicSerializer,
    ProductSerializer,
)


class CategoryAPIView(APIView):
    def get(self, request, query=None):
        if query is None:
            category = get_list_or_404(Category)
            serializer = CategorySerializer(category, many=True)
        elif query.isdigit():
            category = get_object_or_404(Category, id=query)
            serializer = CategorySerializer(category)
        else:
            category = get_object_or_404(Category, slug=query)
            serializer = CategorySerializer(category)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):
    def get(self, request, query=None):
        if query is None:
            product = get_list_or_404(Product)
            serializer = ProductSerializer(product, many=True)
        elif query.isdigit():
            product = get_object_or_404(Product, id=query)
            serializer = ProductSerializer(product)
        else:
            product = get_object_or_404(Product, slug=query)
            serializer = ProductSerializer(product)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get(self, request, category_slug=None, product_slug=None, format=None):
        queryset = Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)


class ProductsListLatestAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:2]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductsBasicListAPIView(APIView):
    def get(self, request, format=None):
        products = get_list_or_404(Product)
        serializer = ProductBasicSerializer(products, many=True)
        return Response(serializer.data)


class CategoryBasicListAPIView(APIView):
    def get(self, request, format=None):
        products = get_list_or_404(Product)
        serializer = CategoryBasicSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
