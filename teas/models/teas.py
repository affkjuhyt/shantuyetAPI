import logging

from django.db import models

from userprofile.models import Owner
from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class Teas(BaseTimeStampModel):
    APPROVED = 'approved'
    REJECT = 'reject'
    PROCESSING = 'processing'

    TEA_STATUS = (
        (APPROVED, 'Approved'),
        (REJECT, 'Reject'),
        (PROCESSING, 'Processing')
    )

    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True)
    age = models.IntegerField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    height = models.FloatField(max_length=2000, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=9)
    lon = models.DecimalField(max_digits=15, decimal_places=9)
    tree_area = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=20, choices=TEA_STATUS, default=PROCESSING)
    image1 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image2 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image3 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)
    image4 = models.ImageField(upload_to="teas/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
