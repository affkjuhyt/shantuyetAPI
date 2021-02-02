import logging

from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from root.authentications import BaseUserJWTAuthentication
from transfer.models import Transfer
from transfer.serializers import TransferSerializer
from userprofile.models import Owner, SecondaryOwner
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from teas.models import Teas
from teas.serializers import TeasSerializer
from userprofile.permissions import SecondaryOwnerOnly
from userprofile.serializers import OwnerSerializer, SecondaryOwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TeasView(ReadOnlyModelViewSet):
    serializer_class = TeasSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

    def get_queryset(self):
        return Teas.objects.filter(status='approved')

    @action(detail=True, methods=['get'], url_path='info_owner', serializer_class=OwnerSerializer)
    def get_info_owner(self, *args, **kwargs):
        tea = self.get_object()
        owner = Owner.objects.filter(teas=tea)
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='info_secondary_owner', serializer_class=OwnerSerializer)
    def get_info_secondary_owner(self, *args, **kwargs):
        tea = self.get_object()
        transfer_ids = Transfer.objects.filter(tea=tea, status='government_agree').values_list('secondary_owner_id', flat=True)
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
    filter_fields = ['status']
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request):
        serializer = TeasSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA)

    def get_queryset(self):
        return Teas.objects.filter()

    @action(detail=True, methods=['post'], url_path='register_transfer', serializer_class=TransferSerializer,
            permission_classes=[SecondaryOwnerOnly])
    def post_register_transfer(self, request, *args, **kwargs):
        tea = self.get_object()
        owner = Owner.objects.filter(teas=tea).first()
        secondary_owner = SecondaryOwner.objects.filter(user_id=request.user.id).first()
        transfer = Transfer.objects.filter(tea=tea, secondary_owner=secondary_owner)
        if len(transfer) != 0:
            return Response('Assignment already exists', status=status.HTTP_400_BAD_REQUEST)
        else:
            Transfer.objects.create(tea=tea,
                                    owner=owner,
                                    secondary_owner=secondary_owner)

            return Response('Register transfer is successfully.', status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='list_request', serializer_class=TransferSerializer)
    def get_list_request(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        tea = self.get_object()
        transfer = Transfer.objects.select_related('tea').filter(tea=tea, status='wait_owner_agree')
        result_page = paginator.paginate_queryset(transfer, request)
        transfer = TransferSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(transfer.data)
