import logging

from django.db import models

from userprofile.models import UserProfile

logger = logging.getLogger(__name__.split('.')[0])


class SecondaryOwner(UserProfile):
    is_enable = models.BooleanField(default=True)
