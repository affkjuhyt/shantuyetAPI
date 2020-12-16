import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from userprofile.permissions import OwnerOnly, SecondaryOwnerOnly
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from request.models import Request
from request.serializers import RequestSerializers

logger = logging.getLogger(__name__.split('.')[0])


class RequestView(ReadOnlyModelViewSet):
    serializer_class = RequestSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Request.objects.filter()


class RequestAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = RequestSerializers
    permission_classes = [AllowAny]
    filter_backends = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Request.objects.filter()
