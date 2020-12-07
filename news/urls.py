from rest_framework_extensions.routers import ExtendedSimpleRouter

from news.apis.v1 import NewsView

public_router = ExtendedSimpleRouter()

public_router.register(
    r'news',
    NewsView,
    basename='v1-news'
)

news_public_urlpatterns = public_router.urls
