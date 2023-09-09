from django.test import TestCase

from friends import services
from friends.errors import FriendError
from friends.models import FriendOffer
from friends.tests.factories import FriendOfferFactory
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for friend services.
    """
    def test_friend_add(self):
        self.assertEqual(0, FriendOffer.objects.count())
        offer = services.friend_add(
            UserFactory(), UserFactory(),
        )
        self.assertEqual(1, FriendOffer.objects.count())
        self.assertEqual(offer, FriendOffer.objects.first())

    def test_friend_add_fail_offer_sent(self):
        offer = FriendOfferFactory()
        with self.assertRaises(FriendError):
            services.friend_add(
                offer.user, offer.other,
            )

    def test_friend_add_fail_already_friend(self):
        user = UserFactory()
        other = UserFactory()
        user.add_friend(other)
        with self.assertRaises(FriendError):
            services.friend_add(user, other)
