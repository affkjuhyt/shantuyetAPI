import logging

from django.db import models

from utils.base_models import BaseModel
from teas.models import Teas
from userprofile.models import UserProfile

logger = logging.getLogger(__name__.split('.')[0])


class Request(BaseModel):
    PROCESSING = 'processing'
    APPROVED = 'approved'
    REJECT = 'reject'

    REQUEST_STATUS = (
        (PROCESSING, 'Processing'),
        (APPROVED, 'Approved'),
        (REJECT, 'Reject')
    )

    tea = models.ForeignKey(Teas, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE, related_name="owner")
    secondary_owner = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE,
                                           related_name="secondary_owner")
    name = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS, default=PROCESSING)
