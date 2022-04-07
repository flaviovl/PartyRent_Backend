from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint signup.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint profile.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     # permission_classes = [permissions.IsAuthenticated]

