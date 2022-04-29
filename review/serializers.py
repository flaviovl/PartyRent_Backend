from rest_framework import serializers

from review.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    client = serializers.CharField(source='client.email')

    class Meta:
        model = Review
        fields = ["id", "star_rating", "client", "product", "comment"]

class ReviewRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def validate_star_rating(self, star_rating):
        if star_rating not in range(1, 6):
            raise serializers.ValidationError("The rating must be an integer between 1 and 5")
        return star_rating

class BasicReviewSerializer(serializers.ModelSerializer):
    # product = serializers.CharField(source='product.name')
    class Meta:
        model = Review
        fields = ["star_rating", "comment"]
