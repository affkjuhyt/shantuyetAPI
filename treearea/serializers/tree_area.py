import logging

from rest_framework import serializers

from teas.models import Teas
from treearea.models import TreeArea

logger = logging.getLogger(__name__.split('.')[0])


class TreeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeArea
        fields = ['id', 'name', 'acreage', 'number_tea', 'content', 'image', 'lat1', 'lon1', 'lat2', 'lon2',
                  'lat3', 'lon3', 'lat4', 'lon4', 'lat5', 'lon5', 'lat6', 'lon6', 'lat7', 'lon7', 'lat8', 'lon8']
        read_only_fields = ['id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['number_tea'] = Teas.objects.filter(tree_area=instance.id).count()

        return response
