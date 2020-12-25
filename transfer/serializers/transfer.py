import logging

from rest_framework import serializers

from transfer.models import Transfer

logger = logging.getLogger(__name__)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'transfer_status']
