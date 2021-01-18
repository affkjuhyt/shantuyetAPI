from rest_framework_extensions.routers import ExtendedSimpleRouter

from userprofile.apis.v1 import UserPublicView, OwnerPublicView, SecondaryOwnerPublicView, OwnerAdminView, \
    SecondaryOwnerAdminView, UpdateInfo, GovernmentAdminView, GovernmentPublicView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'owner',
    OwnerPublicView,
    basename='v1-owner'
)

public_router.register(
    r'secondary_owner',
    SecondaryOwnerPublicView,
    basename='v1-secondary_owner'
)

userprofile_public_urlpatterns = public_router.urls

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'user-profile',
    UserPublicView,
    basename='v1-user-profile'
)

admin_router.register(
    r'owners',
    OwnerAdminView,
    basename='v1-owner'
)

admin_router.register(
    r'secondary_owners',
    SecondaryOwnerAdminView,
    basename='v1-secondary_owner'
)

admin_router.register(
    r'government',
    GovernmentAdminView,
    basename='v1-government'
)

admin_router.register(
    r'update-account',
    UpdateInfo,
    basename='v1-update-account'
)

userprofile_urlpatterns = admin_router.urls
