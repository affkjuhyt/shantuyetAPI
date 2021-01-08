import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from teas.models import Teas
from teas.serializers import TeasSerializer
from transfer.models import Transfer
from transfer.serializers import TransferSerializer
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

    @action(detail=False, methods=['get'], url_path='secondary_owner_teas', serializer_class=TeasSerializer)
    def get_secondary_owner_teas(self, request, **kwargs):
        secondary_owner = SecondaryOwner.objects.filter(user_id=request.user.id).first()
        tea_ids = Transfer.objects.filter(secondary_owner=secondary_owner.id).values_list('tea_id', flat=True)
        teas = Teas.objects.filter(id__in=tea_ids)
        serializer = TeasSerializer(teas, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='manager_transfer', serializer_class=TransferSerializer)
    def get_transfer(self, request, *args, **kwargs):
        secondary_owner = SecondaryOwner.objects.filter(user_id=request.user.id).first()
        transfer = Transfer.objects.filter(secondary_owner=secondary_owner)

        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data)
