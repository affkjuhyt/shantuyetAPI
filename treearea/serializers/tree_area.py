import logging

from rest_framework import serializers

from teas.models import Teas
from treearea.models import TreeArea, Coordinate

logger = logging.getLogger(__name__.split('.')[0])


class TreeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeArea
        fields = ['id', 'name', 'acreage', 'number_tea', 'content', 'image']
        read_only_fields = ['id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        coordinate = Coordinate.objects.filter(tree_area=instance.id)
        response['number_tea'] = Teas.objects.filter(tree_area=instance.id, status='approved').count()
        response['coordinate'] = coordinate.values('lat', 'lon')

        return response


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['id', 'lat', 'lon', 'tree_area']
        read_only_fields = ['id']
