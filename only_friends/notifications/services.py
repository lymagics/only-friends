from users.models import User
from notifications.models import Notification


def notify_create(user: User, name: str, **payload) -> Notification:
    notification = Notification(user=user, name=name, payload=payload)
    notification.full_clean()
    notification.save()
    return notification
