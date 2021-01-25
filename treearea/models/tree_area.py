import logging

from django.db import models

logger = logging.getLogger(__name__.split('.')[0])


class TreeArea(models.Model):
    name = models.CharField(max_length=50)
    acreage = models.FloatField(max_length=20, null=True, blank=True)
    number_tea = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="tree_area/%Y/%m/%d", null=True, blank=True)
    lat1 = models.DecimalField(decimal_places=9, max_digits=15)
    lon1 = models.DecimalField(decimal_places=9, max_digits=15)
    lat2 = models.DecimalField(decimal_places=9, max_digits=15)
    lon2 = models.DecimalField(decimal_places=9, max_digits=15)
    lat3 = models.DecimalField(decimal_places=9, max_digits=15)
    lon3 = models.DecimalField(decimal_places=9, max_digits=15)
    lat4 = models.DecimalField(decimal_places=9, max_digits=15)
    lon4 = models.DecimalField(decimal_places=9, max_digits=15)
    lat5 = models.DecimalField(decimal_places=9, max_digits=15)
    lon5 = models.DecimalField(decimal_places=9, max_digits=15)
    lat6 = models.DecimalField(decimal_places=9, max_digits=15)
    lon6 = models.DecimalField(decimal_places=9, max_digits=15)
    lat7 = models.DecimalField(decimal_places=9, max_digits=15)
    lon7 = models.DecimalField(decimal_places=9, max_digits=15)
    lat8 = models.DecimalField(decimal_places=9, max_digits=15)
    lon8 = models.DecimalField(decimal_places=9, max_digits=15)

    def __str__(self):
        return "%s" % self.name
