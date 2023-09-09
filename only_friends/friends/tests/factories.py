import factory
from factory.django import DjangoModelFactory

from friends.models import FriendOffer
from users.tests.factories import UserFactory


class FriendOfferFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    other = factory.SubFactory(UserFactory)

    class Meta:
        model = FriendOffer
