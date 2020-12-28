import logging

from django.db import models

from userprofile.models import UserProfile, Owner
from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class Teas(BaseTimeStampModel):
    HAVE_SECONDARY_OWNER = 'have_secondary_owner'
    NO_SECODARY_OWNER = 'no_secondary_owner'
    TRANSFER_IN_PROGRESS = 'transfer_in_progress'

    TEA_STATUS = (
        (HAVE_SECONDARY_OWNER, 'Have secondary owner'),
        (NO_SECODARY_OWNER, 'No secondary owner'),
        (TRANSFER_IN_PROGRESS, 'Transfer in progress')
    )

    owner = models.ForeignKey(Owner, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True)
    age = models.IntegerField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    height = models.FloatField(max_length=2000, null=True)
    status = models.CharField(max_length=20, choices=TEA_STATUS, default=NO_SECODARY_OWNER)
    lat = models.DecimalField(max_digits=15, decimal_places=9)
    lon = models.DecimalField(max_digits=15, decimal_places=9)
    image1 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image2 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image3 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image4 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
