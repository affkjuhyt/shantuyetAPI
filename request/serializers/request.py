import logging

from rest_framework import serializers

from request.models import Request

logger = logging.getLogger(__name__)


class RequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'request_status']
