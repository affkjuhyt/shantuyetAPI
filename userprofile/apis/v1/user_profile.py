import logging

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import GenericViewSet

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializers

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(GenericViewSet):
    serializer_class = UserProfileSerializers
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user.id).all()
