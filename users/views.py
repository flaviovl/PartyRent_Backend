from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserMiniSerializer, UserSignupSerializer


# =================================================================================================================
# Lembrar criar e mover para utils.py
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# =================================================================================================================
class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        required_fields = {
            
            "meta_optional": 'Fields optional in the request body',
            "is_admin": "bool",
            "username": "str",
            "phone_number": "int",
            "birth_date": "date",
            "picture": "image file",
            "----------------------":"----------------------",
            "meta_required": 'Fields are required in the request body',
            "email": "email",
            "password": "",
            "password2": "",
        }
        return Response(required_fields)

class SigninAPIView(APIView):
    def get(self, request, *args, **kwargs):
        required_fields = {
            
            "meta": 'Fields are required in the request body',
            "email": "email",
            "password": "",
        }
        return Response(required_fields)
    
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'error': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, username=email, password=password)
        if user is None:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)

class SignoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ListDetailUserAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]            # somnente o admin pode listar usuários

    def get(self, request, query=None):
        if query is None:
            users = User.objects.all()
            serializer = UserMiniSerializer(users, many=True)
        else:
            # users = User.objects.filter(username__icontains=query)
            users = User.objects.filter(id=query)
            serializer = UserSignupSerializer(users, many=True)
        return Response(serializer.data)
