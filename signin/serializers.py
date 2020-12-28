import logging

from rest_auth.serializers import UserModel
from rest_framework import serializers

logger = logging.getLogger(__name__)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
