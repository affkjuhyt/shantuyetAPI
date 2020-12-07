from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from news.urls import news_public_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="SAMPLE API",
        default_version='v1',
        description="SAMPLE API DOCS",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/public', include(news_public_urlpatterns)),
]
