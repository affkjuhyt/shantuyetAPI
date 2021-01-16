import logging

from rest_framework import serializers

from teas.models import Teas
from treearea.models import TreeArea

logger = logging.getLogger(__name__.split('.')[0])


class TreeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeArea
        fields = ['id', 'name', 'acreage', 'number_tea', 'content']
        read_only_fields = ['id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['number_tea'] = Teas.objects.filter(tree_area=instance.id).count()

        location = {}
        teas = Teas.objects.filter(tree_area=instance.id)
        for index, tea in enumerate(teas):
            location['lat '+str(index)] = tea.lat
            location['lon '+str(index)] = tea.lon
        response['location']= location
        return response
