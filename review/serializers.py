from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ["client", "product", "star_rating", "comment"]

