from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RentalOrder
from .serializers import RentalOrderDetailSerializer, RentalOrderListSerializer


class RentalOrderUserListAPIView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = get_list_or_404(RentalOrder, user=request.user)
        serializer = RentalOrderListSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalOrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RentalOrderUserDetailAPIView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = get_list_or_404(RentalOrder, user=request.user)
        serializer = RentalOrderDetailSerializer(orders, many=True)
        return Response(serializer.data)


class RentalOrderListAPIView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]            # somente o admin pode listar todas as orders

    def get(self, request, pk=None, format=None):
        if pk is None:
            orders = get_list_or_404(RentalOrder)
            many = True
        else:
            orders = get_object_or_404(RentalOrder, pk=pk)
            many = False
        
        serializer = RentalOrderDetailSerializer(orders, many=many)
        return Response(serializer.data)
