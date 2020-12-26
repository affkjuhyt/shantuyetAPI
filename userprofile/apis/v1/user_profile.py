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


class UserPublicView(GenericViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user.id).all()

    def list(self, request, *args, **kwargs):
        user_profile = self.get_queryset().first()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='owner_teas', serializer_class=TeasSerializer)
    def get_owner_tea(self, *args, **kwargs):
        owner = self.get_object()
        teas = Teas.objects.filter(owner=owner)
        serializer = TeasSerializer(teas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='secondary_owner_teas',
            serializer_class=TeasSerializer)
    def get_secondary_owner_teas(self, *args, **kwargs):
        secondary_owner = self.get_object()
        transfers = Transfer.objects.filter(secondary_owner=secondary_owner)
        if len(transfers) == 0:
            return Response({"message": "Khong co san pham"})

        for transfer in transfers:
            teas = Teas.objects.filter(id=transfer.id)
            serializer = TeasSerializer(teas, many=True)
            return Response(serializer.data)
