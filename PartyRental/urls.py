from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users import urls as user_routes

router = DefaultRouter()
router.registry.extend(user_routes.router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
