from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users import urls as user_routes
from product import urls as product_routes

router = DefaultRouter()
router.registry.extend(user_routes.router.registry)
router.registry.extend(product_routes.router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
