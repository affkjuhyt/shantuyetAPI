import logging

from django.db import models

logger = logging.getLogger(__name__.split('.')[0])


class TreeArea(models.Model):
    name = models.CharField(max_length=50)
    acreage = models.FloatField(max_length=20, null=True, blank=True)
    content = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="tree_area/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

    @property
    def number_tea(self):
        return self.teas_set.all().count()


class Coordinate(models.Model):
    tree_area = models.ForeignKey(TreeArea, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.DecimalField(decimal_places=9, max_digits=15, null=True, blank=True)
    lon = models.DecimalField(decimal_places=9, max_digits=15, null=True, blank=True)

    def __str__(self):
        return "%s" % self.id