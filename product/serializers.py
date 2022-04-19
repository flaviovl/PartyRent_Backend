from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            'name',
            'description',
            'weight',
            'active',
            'price',
            'teste',
            'category'
        ]    


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'