from django.db.models import Avg
from rest_framework import serializers
from review.models import Review

from product.models import Category, Product


# from review.serializers import BasicReviewSerializer
class ProductBasicSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            # "slug",
            "price",
            "category",
        ]
        # depth = 1
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    # product_reviews = BasicReviewSerializer(many=True)       # category_products = related_name
    
    # average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            # "slug",
            "price",
            "description",
            "category",
            # "average_rating",
            # "product_reviews",
            "endpoint_pk",
            "endpoint_slug",
            "path_pk",
            "path_slug",
            "image_url",
            "thumbnail_url",
        ]
        # depth = 1

    # def get_average_rating(self, obj):
    #     average = obj.product_reviews.aggregate(Avg('star_rating')).get('star_rating__avg')
    #     if average is None:
    #         return 0
    #     return round(average, 2)
class CategoryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]
class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(many=True)       # category_products = related_name

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "category_products"
        ]


# # class InvetorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invetory
#         fields = ['id', 'store_price', 'quantity']
