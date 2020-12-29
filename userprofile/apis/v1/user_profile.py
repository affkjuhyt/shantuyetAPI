import logging

from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from transfer.models import Transfer
from root.authentications import BaseUserJWTAuthentication
from teas.models import Teas
from teas.serializers import TeasSerializer
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user).all()

    def list(self, request, *args, **kwargs):
        user_profile = self.get_queryset().first()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)
