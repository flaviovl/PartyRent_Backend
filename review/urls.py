from django.urls import path

from .views import ReviewAPIView, ReviewProductAPIView, ReviewUserAPIView

urlpatterns = [
    path("review/", ReviewAPIView.as_view()),
    path("review/<int:pk>", ReviewAPIView.as_view()),
    path("review/user/<int:pk>", ReviewUserAPIView.as_view()),
    path("review/product/", ReviewProductAPIView.as_view()),
    path("review/product/<str:query>", ReviewProductAPIView.as_view()),
]
