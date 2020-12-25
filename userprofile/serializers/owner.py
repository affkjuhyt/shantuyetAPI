import logging

from rest_framework import serializers

from userprofile.models import UserProfile

logger = logging.getLogger(__name__.split('.')[0])


class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'fullname', 'phone_number', 'email', 'dob', 'gender', 'address',
                  'user_type', 'id_card', 'is_deleted', 'permanent_residence', 'issued_by', 'issued_date', 'province',
                  'district', 'sub_district', 'street']