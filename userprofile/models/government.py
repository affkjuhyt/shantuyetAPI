import logging

from django.db import models

from userprofile.models import UserProfile

logger = logging.getLogger(__name__.split('.')[0])


class Government(UserProfile):
    city = models.CharField(max_length=30, null=True, blank=True)
    district = models.CharField(max_length=30, null=True, blank=True)
    wards = models.CharField(max_length=30, null=True, blank=True)
    village = models.CharField(max_length=30, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
