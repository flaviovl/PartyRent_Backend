from django.urls import path

from .views import (
    CategoryAPIView,
    CategoryProductAPIView,
    ProductAPIView,
    ProductDetailAPIView,
    ProductsBasicListAPIView,
    ProductsListLatestAPIView,
)

urlpatterns = [
    path("category/", CategoryAPIView.as_view()),
    path("category/<str:query>/", CategoryAPIView.as_view()),
    path("product/", ProductsBasicListAPIView.as_view()),
    path("product/all/", ProductAPIView.as_view()),
    path("product/latest/", ProductsListLatestAPIView.as_view()),
    path("product/<str:query>/", ProductAPIView.as_view()),
    path("product/category/<str:query>/", CategoryProductAPIView.as_view()),
    path("<slug:category_slug>/<slug:product_slug>/", ProductDetailAPIView.as_view()),
]
