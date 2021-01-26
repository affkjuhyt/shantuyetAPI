import logging

from rest_framework import generics, status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from teas.serializers import TeasSerializer
from transfer.models import Transfer
from treearea.models import TreeArea
from teas.models import Teas
from userprofile.models import Owner
from userprofile.models import SecondaryOwner
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import Government
from userprofile.serializers import GovernmentSerializer, SecondaryOwnerSerializer
from userprofile.permissions import GovernmentOnly

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
    permission_classes = [GovernmentOnly]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        return Government.objects.filter()

    @action(detail=False, methods=['get'], url_path='statistics')
    def get_statistics(self, *args, **kwargs):
        statistics_data = []
        number_tree_area = TreeArea.objects.count()
        number_tea = Teas.objects.filter(status='approved').count()
        number_owner = Owner.objects.count()
        number_secondary_owner = SecondaryOwner.objects.filter(status='approved').count()
        statistics_data.append({'number_tree_area': number_tree_area,
                                'number_tea': number_tea,
                                'number_owner': number_owner,
                                'number_secondary_owner': number_secondary_owner})

        return Response(statistics_data)

    @action(detail=False, methods=['post'], url_path='owner_list_teas', serializer_class=TeasSerializer)
    def get_owner_list_tea(self, request, *args, **kwargs):
        owner_id = int(request.data['owner_id'])
        owner = Owner.objects.filter(id=owner_id).first()
        if not owner:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            teas = Teas.objects.filter(owner=owner)
            serializer = TeasSerializer(teas, context={"request": request}, many=True)

            return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='secondary_owner_list_teas', serializer_class=TeasSerializer)
    def get_secondary_owner_list_teas(self, request, **kwargs):
        secondary_owner_id = int(request.data['secondary_owner_id'])
        secondary_owner = SecondaryOwner.objects.filter(id=secondary_owner_id).first()
        if not secondary_owner:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            tea_ids = Transfer.objects.filter(secondary_owner=secondary_owner.id).values_list('tea_id', flat=True)
            teas = Teas.objects.filter(id__in=tea_ids)
            serializer = TeasSerializer(teas, context={"request": request}, many=True)

            return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='process_request_add_tea', serializer_class=TeasSerializer)
    def post_process_request_add_teas(self, request, **kwargs):
        tea = request.data['tea_id']
        request_type = request.data['request_type']
        if request_type == 'approve':
            Teas.objects.filter(id=tea).update(status='approved')
        else:
            Teas.objects.filter(id=tea).update(status='reject')
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='process_request_add_user',
            serializer_class=SecondaryOwnerSerializer)
    def post_process_request_add_user(self, request, *args, **kwargs):
        secondary_owner = request.data['secondary_owner_id']
        request_type = request.data['request_type']
        if request_type == 'approve':
            SecondaryOwner.objects.filter(id=secondary_owner).update(status='approved')
        else:
            SecondaryOwner.objects.filter(id=secondary_owner).update(status='reject')
        return Response(status=status.HTTP_200_OK)
