import logging

from rest_framework import serializers

from userprofile.models import Government

logger = logging.getLogger(__name__.split('.')[0])


class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = ['id', 'user', 'fullname', 'phone_number', 'email', 'dob', 'gender', 'address', 'status',
                  'user_type', 'id_card', 'is_deleted', 'permanent_residence', 'issued_by', 'issued_date', 'province',
                  'district', 'sub_district', 'street', 'front_view_photo', 'back_view_photo']
        read_only_fields = ['id']