import logging

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from root.authentications import BaseUserJWTAuthentication
from transfer.models import Transfer
from userprofile.models import Owner, SecondaryOwner
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from teas.models import Teas
from teas.serializers import TeasSerializer
from userprofile.serializers import OwnerSerializer, SecondaryOwnerSerializer, UserProfileSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TeasView(ReadOnlyModelViewSet):
    serializer_class = TeasSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

    def get_queryset(self):
        return Teas.objects.filter()

    @action(detail=True, methods=['get'], url_path='info_owner', serializer_class=OwnerSerializer)
    def get_info_owner(self, *args, **kwargs):
        tea = self.get_object()
        owner = Owner.objects.filter(teas=tea)
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='info_secondary_owner', serializer_class=OwnerSerializer)
    def get_info_secondary_owner(self, *args, **kwargs):
        tea = self.get_object()
        transfer_ids = Transfer.objects.filter(tea=tea).values_list('secondary_owner_id', flat=True)
        if len(transfer_ids) == 0:
            return Response({"message": "Khong co chu so huu thu cap"})

        secondary_owner = SecondaryOwner.objects.filter(id__in=transfer_ids)
        serializer = SecondaryOwnerSerializer(secondary_owner, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='info-user')
    def get_info_user(self, *args, **kwargs):
        tea = self.get_object()
        info_user_data = []
        info_user_data.append({'tea': TeasSerializer(tea).data})

        return Response({'data': info_user_data})


class TeasAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = TeasSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    filter_backends = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Teas.objects.filter().all()
