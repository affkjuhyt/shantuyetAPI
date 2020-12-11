import logging

from django.db import models

from utils.base_models import BaseUserModel

logger = logging.getLogger(__name__.split('.')[0])


class UserProfile(BaseUserModel):

    fullname = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=False, blank=False)
    sex = models.BooleanField(default=False)
    address = models.CharField(max_length=70, null=True, blank=True)
    ssn = models.CharField(max_length=12, null=True, blank=True)