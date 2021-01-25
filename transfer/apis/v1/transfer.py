import logging

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin
from rest_framework.response import Response

from root.authentications import BaseUserJWTAuthentication
from transfer.models import Transfer
from transfer.serializers import TransferSerializer
from userprofile.permissions import OwnerOnly, GovernmentOnly

logger = logging.getLogger(__name__.split('.')[0])


class TransferView(ReadOnlyModelViewSet):
    serializer_class = TransferSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Transfer.objects.filter()


class TransferAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = TransferSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    filter_backends = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Transfer.objects.filter()

    @action(detail=False, methods=['post'], url_path='accept_requests', permission_classes=[OwnerOnly])
    def post_approved_request(self, request, *args, **kwargs):

        try:
            tea = request.data['tea']
            secondary_owner = request.data['secondary_owner']
            Transfer.objects.filter(tea=tea, secondary_owner=secondary_owner).update(status='government_agree')
            Transfer.objects.filter(tea=tea).exclude(secondary_owner=secondary_owner).update(status='reject')

            return Response('Approved register transfer successfully!')
        except ValidationError:
            return Response('Error when agreeing to transfer!')

    @action(detail=False, methods=['post'], url_path='reject_requests', permission_classes=[OwnerOnly])
    def post_reject_request(self, request, *args, **kwargs):

        try:
            tea = request.data['tea']
            secondary_owner = request.data['secondary_owner']
            Transfer.objects.filter(tea=tea, secondary_owner=secondary_owner).update(status='reject')

            return Response('Reject register transfer successfully!')
        except ValidationError:
            return Response('Error when reject to transfer!')

    @action(detail=False, methods=['get'], url_path='get_transfer_wait_government', serializer_class=TransferSerializer)
    def get_transfer_government(self, *args, **kwargs):
        transfers = Transfer.objects.filter(status='government_agree')
        transfer = TransferSerializer(transfers, many=True).data

        return Response(transfer)

    @action(detail=False, methods=['post'], url_path='process_request_government', serializer_class=TransferSerializer)
    def post_process_request_government(self, request, *args, **kwargs):
        try:
            transfer_id = request.data['transfer_id']
            request_type = request.data['request_type']
            if request_type == 'approve':
                Transfer.objects.filter(id=transfer_id).update(status='approved')
            else:
                Transfer.objects.filter(id=transfer_id).update(status='reject')
            return Response('Successfully process request')

        except ValidationError:
            return Response('Error when process request')
