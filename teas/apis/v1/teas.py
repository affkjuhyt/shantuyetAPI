import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from userprofile.permissions import OwnerOnly, SecondaryOwnerOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from teas.models import Teas
from teas.serializers import TeasSerializers

logger = logging.getLogger(__name__.split('.')[0])


class TeasView(ReadOnlyModelViewSet):
    serializer_class = TeasSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Teas.objects.filter()


class TeasAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = TeasSerializers
    permission_classes = [AllowAny]
    filter_backends = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Teas.objects.filter()
