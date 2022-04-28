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
            category = Category.objects.all()
        elif query.isdigit():
            category = Category.objects.filter(id=query)
        else:
            category = Category.objects.filter(slug=query)
        
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = CategoryBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductAPIView(APIView):
    def get(self, request, query=None):
        if query is None:
            product = Product.objects.all()
        elif query.isdigit():
            product = Product.objects.filter(id=query)
        else:
            product = Product.objects.filter(slug=query)
        
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        products = Product.objects.all()
        serializer = ProductBasicSerializer(products, many=True)
        return Response(serializer.data)


class CategoryBasicListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = CategoryBasicSerializer(products, many=True)
        return Response(serializer.data)
