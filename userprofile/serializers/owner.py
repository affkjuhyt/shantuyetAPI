import logging

from rest_framework import serializers

from userprofile.models import Owner

logger = logging.getLogger(__name__.split('.')[0])


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'user', 'fullname', 'phone_number', 'email', 'dob', 'gender', 'address', 'status',
                  'user_type', 'id_card', 'is_deleted', 'permanent_residence', 'issued_by', 'issued_date', 'province',
                  'district', 'sub_district', 'street', 'front_view_photo', 'back_view_photo']
        read_only_fields = ['id']