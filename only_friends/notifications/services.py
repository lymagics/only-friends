from django.db import transaction

from users.models import User
from notifications.models import Notification


def notify_create(user: User, name: str, **payload) -> Notification:
    notification = Notification(user=user, name=name, payload=payload)
    notification.full_clean()
    notification.save()
    return notification


@transaction.atomic
def notify_mark_seen(notifications: list[Notification]):
    for notification in notifications:
        notification.seen = True
        notification.save()
