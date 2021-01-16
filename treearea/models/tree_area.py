import logging

from django.db import models

logger = logging.getLogger(__name__.split('.')[0])


class TreeArea(models.Model):
    name = models.CharField(max_length=50)
    acreage = models.FloatField(max_length=20, null=True, blank=True)
    number_tea = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
