import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import SecondaryOwner
from userprofile.serializers import SecondaryOwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class SecondaryOwnerPublicView(ReadOnlyModelViewSet):
    serializer_class = SecondaryOwnerSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return SecondaryOwner.objects.filter()


class SecondaryOwnerAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = SecondaryOwnerSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return SecondaryOwner.objects.filter()
