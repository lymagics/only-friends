import factory
from factory.django import DjangoModelFactory

from friends.models import FriendOffer
from users.tests.factories import UserFactory
from notifications.tests.factories import NotificationFactory


class FriendOfferFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    other = factory.SubFactory(UserFactory)
    notification = factory.SubFactory(NotificationFactory)

    class Meta:
        model = FriendOffer
