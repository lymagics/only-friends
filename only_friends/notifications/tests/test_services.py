from django.test import TestCase

from users.tests.factories import UserFactory
from notifications import services
from notifications.models import Notification


class TestServices(TestCase):
    """
    Test case for notification services.
    """
    def test_notify_create(self):
        self.assertEqual(0, Notification.objects.count())
        notification = services.notify_create(
            UserFactory(), 'notify', message='message',
        )
        self.assertEqual(1, Notification.objects.count())
        self.assertEqual(notification, Notification.objects.first())
