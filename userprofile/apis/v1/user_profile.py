import logging

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user.id).all()
