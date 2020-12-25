import logging

from rest_framework import serializers

from teas.models import Teas

logger = logging.getLogger(__name__)


class TeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teas
        fields = ['id', 'owner', 'name', 'age', 'diameter', 'lat', 'lon',
                  'image1', 'image2', 'image3', 'image4']
