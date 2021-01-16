from rest_framework_extensions.routers import ExtendedSimpleRouter

from treearea.apis.v1 import TreeAreaPublicView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'tree_area',
    TreeAreaPublicView,
    basename='v1-tree-area'
)

tree_area_public_urlpatterns = public_router.urls