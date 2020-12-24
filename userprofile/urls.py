from rest_framework_extensions.routers import ExtendedSimpleRouter

from userprofile.apis.v1 import UserPublicView, OwnerView, SecondaryOwnerView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'non-users',
    UserPublicView,
    basename='v1-non-user'
)

public_router.register(
    r'owners',
    OwnerView,
    basename='v1-owner'
)

public_router.register(
    r'secondary-owners',
    SecondaryOwnerView,
    basename='v1-secondary-owner'
)

userprofile_public_urlpatterns = public_router.urls

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'non-users',
    UserPublicView,
    basename='v1-non-user'
)

admin_router.register(
    r'owners',
    OwnerView,
    basename='v1-owner'
)

admin_router.register(
    r'secondary-owners',
    SecondaryOwnerView,
    basename='v1-secondary-owner'
)

userprofile_urlpatterns = admin_router.urls
