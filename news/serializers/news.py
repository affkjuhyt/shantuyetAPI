import logging

from rest_framework import serializers

from news.models import News

logger = logging.getLogger(__name__)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'is_enable', 'is_hot', 'thumbnail', 'short_content', 'content', 'date_modified',
                  'date_added']
        read_only_fields = ['id', 'is_enable']
