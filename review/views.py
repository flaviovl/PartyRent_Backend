from rest_framework import viewsets

from .models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

