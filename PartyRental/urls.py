from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from product import urls as product_routes
from rest_framework.routers import DefaultRouter
from review import urls as review_routes
from shoppingcart import urls as cart_routes
from users import urls as user_routes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.registry.extend(user_routes.router.registry)
router.registry.extend(product_routes.router.registry)
router.registry.extend(cart_routes.router.registry)
router.registry.extend(review_routes.router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Party Rental API",
        default_version='v1',
        description="A API e voltada a realização de aluguel para artigos diversos para festas.",
        contact=openapi.Contact(email="contact@partyrental.local"),
        license=openapi.License(name="FGA License"),
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())

]

# swagger
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

