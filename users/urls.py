from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()

router.register(r"users", UserViewSet, basename="user",)
router.register(r"users/signup", UserViewSet, basename="register",)
