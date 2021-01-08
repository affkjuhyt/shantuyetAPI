import logging

from rest_framework import serializers

from transfer.models import Transfer
from userprofile.models import SecondaryOwner

logger = logging.getLogger(__name__)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'status', 'secondary_owner']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['secondary_owner_name'] = instance.secondary_owner.fullname
        response['tree_area'] = instance.tea.tree_area
        response['owner_name'] = instance.owner.fullname
        response['secondary_owner_address'] = instance.secondary_owner.address
        response['secondary_owner_phone'] = instance.secondary_owner.phone_number
        response['secondary_owner_dob'] = instance.secondary_owner.dob
        response['secondary_owner_email'] = instance.secondary_owner.email
        response['secondary_owner_gender'] = instance.secondary_owner.gender
        response['secondary_owner_province'] = instance.secondary_owner.province
        response['secondary_owner_district'] = instance.secondary_owner.district
        response['secondary_owner_sub_district'] = instance.secondary_owner.sub_district
        response['secondary_owner_street'] = instance.secondary_owner.street
        response['secondary_owner_id_card'] = instance.secondary_owner.id_card
        response['secondary_owner_permanent'] = instance.secondary_owner.permanent_residence
        response['secondary_owner_issued_by'] = instance.secondary_owner.issued_by
        response['secondary_owner_issued_date'] = instance.secondary_owner.issued_date

        return response
