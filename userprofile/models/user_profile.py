import logging

from django.db import models

from utils.base_models import BaseUserModel

logger = logging.getLogger(__name__.split('.')[0])


class UserProfile(BaseUserModel):
    OWNER = 'owner'
    SECONDARY_OWNER = 'secondary_owner'
    GOVERNMENT = 'government'
    PROCESSING = 'processing'
    APPROVED = 'approved'
    REJECT = 'reject'
    MALE = 'male'
    FEMALE = 'female'

    USERTYPE = (
        (OWNER, 'Owner'),
        (SECONDARY_OWNER, 'SecondaryOwner'),
        (GOVERNMENT, 'Government')
    )

    STATUS = (
        (PROCESSING, 'Processing'),
        (APPROVED, 'Approved'),
        (REJECT, 'Reject')
    )

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=False, blank=False)
    gender = models.CharField(max_length=20,choices=GENDER, default=MALE)
    address = models.CharField(max_length=150, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default=PROCESSING)
    user_type = models.CharField(max_length=20, choices=USERTYPE, default=SECONDARY_OWNER)
    id_card = models.CharField(max_length=12, null=True, blank=True)
    permanent_residence = models.CharField(max_length=2000, null=True, blank=True)
    issued_by = models.CharField(max_length=1000, null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    province = models.CharField(max_length=500, null=True, blank=True)
    district = models.CharField(max_length=500, null=True, blank=True)
    sub_district = models.CharField(max_length=500, null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    front_view_photo = models.ImageField(upload_to="userprofile/%Y/%m/%d", null=True, blank=True)
    back_view_photo = models.ImageField(upload_to="userprofile/%Y/%m/%d", null=True, blank=True)
    image = models.ImageField(upload_to="userprofile/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return "%s" % self.fullname
