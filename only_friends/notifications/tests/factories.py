import factory
from factory.django import DjangoModelFactory

from users.tests.factories import UserFactory
from notifications.models import Notification


class NotificationFactory(DjangoModelFactory):
    name = factory.Faker('word')
    payload = {}
    seen = factory.Faker('pybool')
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Notification
