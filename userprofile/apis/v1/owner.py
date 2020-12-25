import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from teas.models import Teas
from teas.serializers import TeasSerializers
from userprofile.models import Owner
from userprofile.serializers import OwnerSerializers

logger = logging.getLogger(__name__.split('.')[0])


class OwnerPublicView(ReadOnlyModelViewSet):
    serializer_class = OwnerSerializers
    permission_classes = [AllowAny]
    filter_fields = ['current_status']
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Owner.objects.filter()

    @action(detail=True, methods=['get'], url_path='owner_teas', serializer_class=TeasSerializers)
    def get_owner_tea(self, *args, **kwargs):
        owner = self.get_object()
        teas = Teas.objects.filter(owner=owner)
        serializer = TeasSerializers(teas, many=True)
        return Response(serializer.data)


class OwnerAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = OwnerSerializers
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    filter_fields = ['current_status']
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Owner.objects.filter()
