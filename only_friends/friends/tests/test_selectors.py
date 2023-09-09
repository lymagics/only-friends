from django.test import TestCase

from friends import selectors
from friends.tests.factories import FriendOfferFactory


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
