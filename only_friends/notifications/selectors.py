from users.models import User
from notifications.models import Notification


def notify_list(user: User, status: str = 'unseen') -> list[Notification]:
    if status == 'seen':
        return user.notifications.filter(seen=True).all()
    if status == 'unseen':
        return user.notifications.filter(seen=False).all()
    return user.notifications.all()
