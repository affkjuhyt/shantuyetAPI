from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from news.urls import news_public_urlpatterns
from teas.urls import teas_public_urlpatterns, teas_urlpatterns
from treearea.urls import tree_area_public_urlpatterns
from userprofile.urls import userprofile_public_urlpatterns, userprofile_urlpatterns
from transfer.urls import transfer_public_urlpatterns, transfer_urlpatterns
from signin import views


schema_view = get_schema_view(
    openapi.Info(
        title="SAMPLE API",
        default_version='v1',
        description="SAMPLE API DOCS",
    ),
    public=True,
)

external_public_urlpatterns = news_public_urlpatterns + teas_public_urlpatterns + userprofile_public_urlpatterns + \
                              transfer_public_urlpatterns + tree_area_public_urlpatterns
external_urlpatterns = userprofile_urlpatterns + teas_urlpatterns + transfer_urlpatterns

urlpatterns = (
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/public/', include(external_public_urlpatterns)),
    path('v1/', include(external_urlpatterns)),
    path('signingg/', views.GoogleView.as_view(), name='signin-gg'),
    path('signinfb/', views.FacebookView.as_view(), name='signin-fb'),
    path('signinapple/', views.AppleView.as_view(), name='signin-apple'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
)
