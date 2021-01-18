import logging

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from teas.models import Teas
from treearea.models import TreeArea
from treearea.serializers import TreeAreaSerializer
from teas.serializers import TeasSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TreeAreaPublicView(ReadOnlyModelViewSet):
    serializer_class = TreeAreaSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return TreeArea.objects.filter()

    @action(detail=True, methods=['get'], url_path='list_teas', serializer_class=TeasSerializer)
    def get_list_tea(self, *args, **kwargs):
        tree_area = self.get_object()
        tea = Teas.objects.filter(tree_area=tree_area)
        serializer = TeasSerializer(tea, many=True)
        return Response(serializer.data)

