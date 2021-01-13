import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin
from root.authentications import BaseUserJWTAuthentication
from rest_framework.filters import SearchFilter

from news.models import News
from news.serializers import NewsSerializer

logger = logging.getLogger(__name__.split('.')[0])


class NewsView(ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = [SearchFilter]
    filter_fields = ['is_enable', 'is_hot']
    search_fields = ['title']

    def get_queryset(self):
        return News.objects.filter(is_enable=True).order_by('-date_added')


class NewsAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = ['is_enable', 'is_hot']
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return News.objects.filter()
