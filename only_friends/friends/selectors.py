from friends.models import FriendOffer
from users.models import User


def friend_offer_get(user: User, other: User) -> FriendOffer:
    return FriendOffer.objects.filter(user=user, other=other).first()


def friend_list(user: User) -> list[User]:
    return user.friends.all()
