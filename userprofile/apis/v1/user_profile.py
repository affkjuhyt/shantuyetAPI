import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin
from rest_framework.permissions import AllowAny

from userprofile.models import UserProfile
from userprofile.permissions import OwnerOnly
from userprofile.permissions import SecondaryOwnerOnly
from userprofile.serializers import UserProfileSerializers

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter()


class OwnerView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = UserProfileSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_type='owner')


class SecondaryOwnerView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = UserProfileSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_type='secondary_owner')
