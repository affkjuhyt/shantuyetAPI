import logging

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import ViewSetMixin, GenericViewSet
from rest_framework.permissions import AllowAny

from userprofile.models import UserProfile
from root.authentications import BaseUserJWTAuthentication
from userprofile.serializers import UserProfileSerializers

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(GenericViewSet):
    serializer_class = UserProfileSerializers
    authentication_classes = [BaseUserJWTAuthentication]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user.id).all()

    def list(self, request, *args, **kwargs):
        user_profile = self.get_queryset().first()
        serializer = self.get_serializer(user_profile)
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
