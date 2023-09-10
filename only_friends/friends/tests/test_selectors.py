from django.test import TestCase

from friends import selectors
from friends.tests.factories import FriendOfferFactory
from users.tests.factories import UserFactory


class TestSelectors(TestCase):
    """
    Test case for friend selectors.
    """
    def test_friend_offer_get(self):
        new_offer = FriendOfferFactory()
        offer = selectors.friend_offer_get(
            new_offer.user, new_offer.other
        )
        self.assertEqual(offer, new_offer)

    def test_friend_list(self):
        user = UserFactory()
        other = UserFactory()
        user.add_friend(other)
        friends = selectors.friend_list(user)
        self.assertIn(other, friends)
