from rest_framework_extensions.routers import ExtendedSimpleRouter

from news.apis.v1 import NewsView, NewsAdminView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'news',
    NewsView,
    basename='v1-news'
)

news_public_urlpatterns = public_router.urls

admin_router = ExtendedSimpleRouter()

admin_router.register(
    r'news',
    NewsAdminView,
    basename='v1-news'
)

news_urlpatterns = admin_router.urls
