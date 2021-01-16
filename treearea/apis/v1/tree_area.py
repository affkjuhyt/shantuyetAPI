import logging

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from treearea.models import TreeArea
from treearea.serializers import TreeAreaSerializer

logger = logging.getLogger(__name__.split('.')[0])


class TreeAreaPublicView(ReadOnlyModelViewSet):
    serializer_class = TreeAreaSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return TreeArea.objects.filter()
