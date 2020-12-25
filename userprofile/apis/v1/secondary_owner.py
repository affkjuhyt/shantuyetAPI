import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from request.models import Request
from root.authentications import BaseUserJWTAuthentication
from teas.models import Teas
from teas.serializers import TeasSerializer
from userprofile.models import SecondaryOwner
from userprofile.serializers import SecondaryOwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class SecondaryOwnerPublicView(ReadOnlyModelViewSet):
    serializer_class = SecondaryOwnerSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return SecondaryOwner.objects.filter()

    # @action(detail=True, methods=['get'], url_path='secondary_owner_teas',
    #         serializer_class=TeasSerializers)
    # def get_secondary_owner_teas(self, *args, **kwargs):
    #     secondary_owner = self.get_object()
    #     requests = Request.objects.filter(secondary_owner=secondary_owner)
    #     if len(requests) == 0:
    #         return Response({"message": "Khong co"})
    #
    #     for request in requests:
    #         teas = Teas.objects.filter(id=request.id)
    #         serializer = TeasSerializers(teas, many=True)
    #         return Response(serializer.data)


class SecondaryOwnerAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = SecondaryOwnerSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return SecondaryOwner.objects.filter()
