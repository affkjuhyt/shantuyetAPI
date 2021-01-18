import logging

from rest_framework import serializers

from transfer.models import Transfer
from treearea.models import TreeArea

logger = logging.getLogger(__name__)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'status', 'secondary_owner']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        secondary_owner = instance.secondary_owner

        response['secondary_owner_name'] = secondary_owner.fullname
        tree_area = TreeArea.objects.filter(teas=instance.tea.id).first()
        if tree_area is not None:
            response['tree_area'] = tree_area.name
        else:
            response['tree_area'] = ""
        response['owner_name'] = instance.owner.fullname
        response['secondary_owner_address'] = secondary_owner.address
        response['secondary_owner_phone'] = secondary_owner.phone_number
        response['secondary_owner_dob'] = secondary_owner.dob
        response['secondary_owner_email'] = secondary_owner.email
        response['secondary_owner_gender'] = secondary_owner.gender
        response['secondary_owner_province'] = secondary_owner.province
        response['secondary_owner_district'] = secondary_owner.district
        response['secondary_owner_sub_district'] = secondary_owner.sub_district
        response['secondary_owner_street'] = secondary_owner.street
        response['secondary_owner_id_card'] = secondary_owner.id_card
        response['secondary_owner_permanent'] = secondary_owner.permanent_residence
        response['secondary_owner_issued_by'] = secondary_owner.issued_by
        response['secondary_owner_issued_date'] = secondary_owner.issued_date
        if secondary_owner.front_view_photo:
            response['secondary_owner_front'] = secondary_owner.front_view_photo.url
        else:
            response['secondary_owner_front'] = None

        if secondary_owner.back_view_photo:
            response['secondary_owner_back'] = secondary_owner.back_view_photo.url
        else:
            response['secondary_owner_back'] = None

        return response
