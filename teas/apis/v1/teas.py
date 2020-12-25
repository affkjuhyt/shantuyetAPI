import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from transfer.models import Transfer
from userprofile.models import Owner, SecondaryOwner
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from teas.models import Teas
from teas.serializers import TeasSerializer
from userprofile.serializers import OwnerSerializer, SecondaryOwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TeasView(ReadOnlyModelViewSet):
    serializer_class = TeasSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Teas.objects.filter()


class TeasAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = TeasSerializer
    permission_classes = [AllowAny]
    filter_backends = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Teas.objects.filter().all()

    @action(detail=True, methods=['get'], url_path='info_owner', serializer_class=OwnerSerializer)
    def get_info_owner(self, *args, **kwargs):
        tea = self.get_object()
        owner = Owner.objects.filter(teas=tea)
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='info_secondary_owner', serializer_class=OwnerSerializer)
    def get_info_secondary_owner(self, *args, **kwargs):
        tea = self.get_object()
        transfers = Transfer.objects.filter(tea=tea)
        if len(transfers) == 0:
            return Response({"message": "Khong co chu so huu thu cap"})

        for transfer in transfers:
            secondary_owner = SecondaryOwner.objects.filter(secondary_owner=transfer)
            serializer = SecondaryOwnerSerializer(secondary_owner, many=True)
            return Response(serializer.data)
