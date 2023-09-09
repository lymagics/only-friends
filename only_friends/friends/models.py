from django.conf import settings
from django.db import models

from core.models import BaseModel


class FriendOffer(BaseModel):
    """
    Friend offer entity.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='offers_sent'
    )
    other = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='offers_received',
    )

    def accept(self):
        self.other.add_friend(self.user)
        self.user.add_friend(self.other)
        self.delete()

    def refuse(self):
        self.delete()
