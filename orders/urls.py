from django.urls import path

from .views import (
    RentalOrderListAPIView,
    RentalOrderUserDetailAPIView,
    RentalOrderUserListAPIView,
)

urlpatterns = [
    path("rentalorder/user", RentalOrderUserListAPIView.as_view()),
    path("rentalorder/detail", RentalOrderUserDetailAPIView.as_view()),
    path("rentalorder/all", RentalOrderListAPIView.as_view()),
]
