from pydoc import cli

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review
from .serializers import (
    BasicReviewSerializer,
    ReviewListSerializer,
    ReviewRegisterSerializer,
)


class ReviewAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            review = get_list_or_404(Review)
            serializer = ReviewListSerializer(review, many=True)
        else:
            review = get_object_or_404(Review, id=pk)
            serializer = ReviewListSerializer(review)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReviewUserAPIView(APIView):
    def get(self, request, pk=None, format=None):
        print(pk)
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        qs_review = get_list_or_404(Review, client=pk)
        serializer = ReviewListSerializer(qs_review, many=True)
        return Response(serializer.data)

class ReviewProductAPIView(APIView):
    def get(self, request, query=None, format=None):
        if query is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif query.isdigit():
            qs_review = get_list_or_404(Review, product=query)
        else:
            qs_review = get_list_or_404(Review, product__slug=query)
        serializer = ReviewListSerializer(qs_review, many=True)
        return Response(serializer.data)
