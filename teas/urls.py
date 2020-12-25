from rest_framework_extensions.routers import ExtendedSimpleRouter

from teas.apis.v1 import TeasView, TeasAdminView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'teas',
    TeasView,
    basename='v1-teas'
)

teas_public_urlpatterns = public_router.urls

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'teas',
    TeasAdminView,
    basename='v1-teas'
)

teas_urlpatterns = admin_router.urls
