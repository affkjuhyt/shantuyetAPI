from rest_framework_extensions.routers import ExtendedSimpleRouter

from request.apis.v1 import RequestView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'request',
    RequestView,
    basename='v1-request'
)

request_public_urlpatterns = public_router.urls
