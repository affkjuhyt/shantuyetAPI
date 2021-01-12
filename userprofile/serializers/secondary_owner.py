import logging

from rest_framework import serializers

from transfer.models import Transfer
from userprofile.models import SecondaryOwner

logger = logging.getLogger(__name__.split('.')[0])


class SecondaryOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryOwner
        fields = ['id', 'user', 'fullname', 'phone_number', 'email', 'dob', 'gender', 'address',
                  'user_type', 'id_card', 'is_deleted', 'permanent_residence', 'issued_by', 'issued_date', 'province',
                  'district', 'sub_district', 'street', 'front_view_photo', 'back_view_photo']
        read_only_fields = ['id']
