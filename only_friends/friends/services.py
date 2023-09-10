from django.db import transaction

from friends import selectors
from friends.errors import FriendError
from friends.models import FriendOffer
from users.models import User
from notifications.models import Notification


@transaction.atomic
def friend_add(user: User, other: User) -> FriendOffer:
    if user == other:
        error = 'You can\'t be friend with yourself.'
        raise FriendError(error)
    if user.is_friend(other):
        error = 'You are already friends.'
        raise FriendError(error)
    if selectors.friend_offer_get(user, other):
        error = 'You already sent offer.'
        raise FriendError(error)
    if selectors.friend_offer_get(other, user):
        error = 'User already sent you offer.'
        raise FriendError(error)
    
    notification = Notification(
        name='friends_request',
        user=other,
        payload={'from': user.pk},

    )
    notification.save()

    offer = FriendOffer(
        user=user, 
        other=other, 
        notification=notification
    )
    offer.full_clean()
    offer.save()
    return offer


@transaction.atomic
def friend_remove(user: User, other: User):
    if not user.is_friend(other):
        error = 'You are not friends.'
        raise FriendError(error)
    user.remove_friend(other)
    other.remove_friend(user)


@transaction.atomic
def friend_offer_accept(user: User, other: User):
    offer = selectors.friend_offer_get(user, other)
    if offer is None:
        error = 'You didn\'t recieve offer.'
        raise FriendError(error)
    offer.accept()


def friend_offer_refuse(user: User, other: User):
    offer = selectors.friend_offer_get(user, other)
    if offer is None:
        error = 'You didn\'t recieve offer.'
        raise FriendError(error)
    offer.refuse()
