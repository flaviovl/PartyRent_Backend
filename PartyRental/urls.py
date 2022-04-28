from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# from .views import home

schema_view = get_schema_view(
    openapi.Info(
        title="Party Rental API",
        default_version='v1',
        description="A API e voltada a realização de aluguel para artigos diversos para festas.",
        contact=openapi.Contact(email="contact@partyrental.local"),
        license=openapi.License(name="FGA License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('', home, name='api.home'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("product.urls")),
    path("api/", include("shoppingcart.urls")),
    # path("review/", include("review.urls")),
    # path("", include(router.urls)),
    # path('token/', TokenObtainPairView.as_view()),
    # path('token/refresh', TokenRefreshView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
