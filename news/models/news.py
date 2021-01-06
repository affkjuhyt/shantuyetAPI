import logging

from django.db import models

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class News(BaseTimeStampModel):
    title = models.CharField(max_length=2000, null=True)
    short_content = models.CharField(max_length=2000, null=True)
    short_contentxxxx = models.CharField(max_length=2000, null=True)
    content = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='news/%Y/%m/%d/', null=True, blank=True)
    is_hot = models.BooleanField(default=False)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return "%s | %s" % (self.id, self.title)
