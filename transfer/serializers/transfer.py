import logging

from rest_framework import serializers

from transfer.models import Transfer
from userprofile.models import SecondaryOwner

logger = logging.getLogger(__name__)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'status']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['secondary_owner_name'] = instance.secondary_owner.fullname
        response['tree_area'] = instance.tea.tree_area
        response['owner_name'] = instance.owner.fullname
        response['secondary_owner_address'] = instance.secondary_owner.address
        response['secondary_owner_phone'] = instance.secondary_owner.phone_number

        return response
