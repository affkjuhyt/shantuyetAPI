import logging
import sys

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import ViewSetMixin, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from request.models import Request
from teas.serializers import TeasSerializers
from teas.models import Teas
from userprofile.models import UserProfile
from root.authentications import BaseUserJWTAuthentication
from userprofile.serializers import UserProfileSerializers

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializers
    # authentication_classes = [BaseUserJWTAuthentication]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter().all()

    @action(detail=True, methods=['get'], url_path='owner_teas', serializer_class=TeasSerializers)
    def get_owner_tea(self, *args, **kwargs):
        owner = self.get_object()
        teas = Teas.objects.filter(owner=owner)
        serializer = TeasSerializers(teas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='secondary_owner_teas',
            serializer_class=TeasSerializers)
    def get_secondary_owner_teas(self, *args, **kwargs):
        secondary_owner = self.get_object()
        requests = Request.objects.filter(secondary_owner=secondary_owner)
        if len(requests) == 0:
            return Response({"message":"Khong co"})

        for request in requests:
            teas = Teas.objects.filter(id=request.id)
            serializer = TeasSerializers(teas, many=True)
            return Response(serializer.data)


class OwnerView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = UserProfileSerializers
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_type='owner')


class SecondaryOwnerView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = UserProfileSerializers
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_type='secondary_owner')
