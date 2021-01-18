import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import Government
from userprofile.serializers import GovernmentSerializer

logger = logging.getLogger(__name__.split('.')[0])


class GovernmentPublicView(ReadOnlyModelViewSet):
    serializer_class = GovernmentSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Government.objects.filter()


class GovernmentAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = GovernmentSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Government.objects.filter()
