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
from userprofile.models import Owner
from userprofile.serializers import OwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class OwnerPublicView(ReadOnlyModelViewSet):
    serializer_class = OwnerSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Owner.objects.filter()


class OwnerAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = OwnerSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Owner.objects.filter()

    @action(detail=False, methods=['get'], url_path='owner_teas', serializer_class=TeasSerializer)
    def get_owner_tea(self, request, *args, **kwargs):
        owner = Owner.objects.filter(user_id=request.user.id).first()
        teas = Teas.objects.filter(owner=owner)
        serializer = TeasSerializer(teas, many=True)
        return Response(serializer.data)
