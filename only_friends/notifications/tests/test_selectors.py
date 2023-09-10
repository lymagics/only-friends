from django.test import TestCase

from users.tests.factories import UserFactory
from notifications import selectors
from notifications.tests.factories import NotificationFactory


class TestSelectors(TestCase):
    """
    Test case for notification selectors.
    """
    def test_notify_list(self):
        user = UserFactory()
        new_notification = NotificationFactory(user=user)
        notifications = selectors.notify_list(user)
        self.assertIn(new_notification, notifications)

        new_notification = NotificationFactory(user=user, seen=True)
        notifications = selectors.notify_list(user, status='seen')
        self.assertIn(new_notification, notifications)

        new_notification = NotificationFactory(user=user)
        notifications = selectors.notify_list(user, status='all')
        self.assertIn(new_notification, notifications)
