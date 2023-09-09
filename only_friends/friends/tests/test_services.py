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

    def test_friend_remove(self):
        user = UserFactory()
        other = UserFactory()
        user.add_friend(other)
        services.friend_remove(user, other)
        self.assertFalse(user.is_friend(other))

    def test_friend_remove_fail(self):
        user = UserFactory()
        other = UserFactory()
        with self.assertRaises(FriendError):
            services.friend_remove(user, other)

    def test_friend_offer_accept(self):
        offer = FriendOfferFactory()
        services.friend_offer_accept(
            offer.user, offer.other,
        )
        self.assertTrue(offer.user.is_friend(offer.other))
        self.assertTrue(offer.other.is_friend(offer.user))

    def test_friend_offer_accept_fail(self):
        with self.assertRaises(FriendError):
            services.friend_offer_accept(
                UserFactory(), UserFactory(),
            )
