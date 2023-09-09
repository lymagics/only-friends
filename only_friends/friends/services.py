from friends import selectors
from friends.errors import FriendError
from friends.models import FriendOffer
from users.models import User


def friend_add(user: User, other: User) -> FriendOffer:
    if user.is_friend(other):
        error = 'You are already friends.'
        raise FriendError(error)
    if selectors.friend_offer_get(user, other):
        error = 'You already sent offer.'
        raise FriendError(error)
    if selectors.friend_offer_get(other, user):
        error = 'User already sent you offer.'
        raise FriendError(error)
    
    offer = FriendOffer(user=user, other=other)
    offer.full_clean()
    offer.save()
    return offer


def friend_remove(user: User, other: User):
    if not user.is_friend(other):
        error = 'You are not friends.'
        raise FriendError(error)
    user.remove_friend(other)
    other.remove_friend(user)


def friend_offer_accept(user: User, other: User):
    offer = selectors.friend_offer_get(user, other)
    if offer is None:
        error = 'You didn\'t recieve offer.'
        raise FriendError(error)
    offer.accept()
