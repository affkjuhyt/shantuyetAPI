import logging

from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from treearea.models import TreeArea
from teas.models import Teas
from userprofile.models import Owner
from userprofile.models import SecondaryOwner
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import Government
from userprofile.serializers import GovernmentSerializer

logger = logging.getLogger(__name__.split('.')[0])


class GovernmentPublicView(ReadOnlyModelViewSet):
    serializer_class = GovernmentSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return Government.objects.filter()


class GovernmentAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = GovernmentSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Government.objects.filter()

    @action(detail=False, methods=['get'], url_path='statistics')
    def get_statistics(self, *args, **kwargs):
        statistics_data = []
        number_tree_area = TreeArea.objects.count()
        number_tea = Teas.objects.count()
        number_owner = Owner.objects.count()
        number_secondary_owner = SecondaryOwner.objects.count()
        statistics_data.append({'number_tree_area': number_tree_area,
                                'number_tea': number_tea,
                                'number_owner': number_owner,
                                'number_secondary_owner': number_secondary_owner})

        return Response(statistics_data)
