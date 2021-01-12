import logging

from rest_framework import serializers

from teas.models import Teas
from transfer.models import Transfer

logger = logging.getLogger(__name__)


class TeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teas
        fields = ['id', 'owner', 'name', 'age', 'diameter', 'lat', 'lon', 'height','tree_area',
                  'image1', 'image2', 'image3', 'image4']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        if instance.owner is not None:
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
                    response['tea_status'] = transfer.status
            else:
                response['secondary_owner_name'] = None
                response['secondary_owner_phone'] = None
                response['secondary_owner_email'] = None
                response['secondary_owner_adrress'] = None
                response['tea_status'] = None

        return response

    def validate(self, data):
        lat = data['lat']
        lon = data['lon']
        if(0 > lat or lat > 90):
            raise serializers.ValidationError("Error")
        if(0 > lon or lon > 90):
            raise serializers.ValidationError("Error")
        return data
