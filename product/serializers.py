from django.db.models import Avg
from rest_framework import serializers
from review.models import Review

from product.models import Category, Product


# from review.serializers import BasicReviewSerializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
        ]
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
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "average_rating",
            "description",
            "slug",
            "endpoint_pk",
            "endpoint_slug",
            "path_pk",
            "path_slug",
            "image_url",
            "thumbnail_url",
        ]
        # depth = 1

    def get_average_rating(self, obj):
        average = obj.product_reviews.aggregate(Avg('star_rating')).get('star_rating__avg')
        if average is None:
            return 0
        return round(average, 2)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "path_pk",
            "path_slug",
        ]
        

class CategoryProductSerializer(serializers.ModelSerializer):
    # products = ProductCategorySerializer(many=True)       # products = related_name

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "path_pk",
            "path_slug",
            # "quantity"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['quantity'] = instance.products.count()
        data['products'] = ProductCategorySerializer(instance.products, many=True).data
        return data
