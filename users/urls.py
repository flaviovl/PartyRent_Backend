from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import ListDetailUserAPIView, SigninAPIView, SignoutAPIView, SignupAPIView

app_name = 'users'

urlpatterns = [
    path('users/', ListDetailUserAPIView.as_view(), name='list-users'),
    path('users/<int:query>/', ListDetailUserAPIView.as_view(), name='user-detail'),
    path('signup/', SignupAPIView.as_view(), name='register'),
    path('signin/', SigninAPIView.as_view(), name='login'),
    path('signout/', SignoutAPIView.as_view(), name='logout'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
