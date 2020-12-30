from rest_framework_extensions.routers import ExtendedSimpleRouter

from transfer.apis.v1 import TransferView, TransferAdminView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'transfer',
    TransferView,
    basename='v1-transfer'
)

transfer_public_urlpatterns = public_router.urls


admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'transfers',
    TransferAdminView,
    basename='v1-transfer'
)

transfer_urlpatterns = admin_router.urls
