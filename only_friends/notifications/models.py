from django.conf import settings
from django.db import models

from core.models import BaseModel


class Notification(BaseModel):
    """
    Notification entity.
    """
    name = models.CharField(max_length=120)
    payload = models.JSONField()
    seen = models.BooleanField(default=False)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
    )

    def __str__(self) -> str:
        return self.name
