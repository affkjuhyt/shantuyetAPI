import logging

from rest_framework import serializers

from teas.models import Teas
from transfer.models import Transfer

logger = logging.getLogger(__name__)


class TeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teas
        fields = ['id', 'owner', 'name', 'age', 'diameter', 'status', 'lat', 'lon', 'height',
                  'image1', 'image2', 'image3', 'image4']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['owner_name'] = instance.owner.fullname
        response['owner_phone'] = instance.owner.phone_number
        response['owner_email'] = instance.owner.email
        response['owner_address'] = instance.owner.address

        transfers = Transfer.objects.filter(tea=instance.id)
        if len(transfers) > 0:
            for transfer in transfers:
                secondary_owner = transfer.secondary_owner
                response['secondary_owner_name'] = secondary_owner.fullname
                response['secondary_owner_phone'] = secondary_owner.phone_number
                response['secondary_owner_email'] = secondary_owner.email
                response['secondary_owner_adrress'] = secondary_owner.address
        else:
            response['secondary_owner_name'] = ""
            response['secondary_owner_phone'] = ""
            response['secondary_owner_email'] = ""
            response['secondary_owner_adrress'] = ""

        return response
