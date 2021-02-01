import logging

from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

from root.authentications import BaseUserJWTAuthentication
from teas.models import Teas
from teas.serializers import TeasSerializer
from transfer.models import Transfer
from userprofile.models import SecondaryOwner
from userprofile.serializers import SecondaryOwnerSerializer

logger = logging.getLogger(__name__.split('.')[0])


class SecondaryOwnerPublicView(ReadOnlyModelViewSet):
    serializer_class = SecondaryOwnerSerializer
    permission_classes = [AllowAny]
    filter_fields = ['status']
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return SecondaryOwner.objects.filter()


class SecondaryOwnerAdminView(ViewSetMixin, generics.RetrieveUpdateAPIView, generics.ListCreateAPIView):
    serializer_class = SecondaryOwnerSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    permission_classes = [AllowAny]
    filter_fields = ['status']
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request):
        serializer = SecondaryOwnerSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA)

    def get_queryset(self):
        return SecondaryOwner.objects.filter()

    @action(detail=False, methods=['get'], url_path='secondary_owner_teas', serializer_class=TeasSerializer)
    def get_secondary_owner_teas(self, request, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        secondary_owner = SecondaryOwner.objects.filter(user_id=request.user.id).first()
        tea_ids = Transfer.objects.filter(secondary_owner=secondary_owner.id).values_list('tea_id', flat=True)
        teas = Teas.objects.filter(id__in=tea_ids)
        result_page = paginator.paginate_queryset(teas, request)
        serializer = TeasSerializer(result_page, context={"request": request}, many=True)

        return paginator.get_paginated_response(serializer.data)
