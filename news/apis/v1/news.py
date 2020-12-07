import logging

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from news.models import News
from news.serializers import NewsSerializer

logger = logging.getLogger(__name__.split('.')[0])


class NewsView(ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    filter_fields = ['is_enable', 'is_hot']
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        user = User.objects.all()
        return News.objects.filter(is_enable=True)
