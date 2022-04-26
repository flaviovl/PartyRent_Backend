from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import ListDetailUserAPIView, SigninAPIView, SignoutAPIView, SignupAPIView

app_name = 'users'

urlpatterns = [
    path('user/', ListDetailUserAPIView.as_view(), name='list-users'),
    path('user/<int:query>/', ListDetailUserAPIView.as_view(), name='user-detail'),
    path('user/signup/', SignupAPIView.as_view(), name='register'),
    path('user/signin/', SigninAPIView.as_view(), name='login'),
    path('user/signout/', SignoutAPIView.as_view(), name='logout'),
    path('user/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
