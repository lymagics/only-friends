from django.conf import settings
from django.db import models

from core.models import BaseModel
from notifications.models import Notification


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
    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
    )

    def accept(self):
        self.other.add_friend(self.user)
        self.user.add_friend(self.other)
        self.notification.delete()
        self.delete()

    def refuse(self):
        self.notification.delete()
        self.delete()
