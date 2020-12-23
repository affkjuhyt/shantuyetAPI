from django.db import models
from django.conf import settings


class BaseTimeStampModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseUserModel(BaseTimeStampModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user"
    )

    class Meta:
        abstract = True


class BaseModel(BaseTimeStampModel):
    class Meta:
        abstract = True
