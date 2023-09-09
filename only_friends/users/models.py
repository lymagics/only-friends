from django.contrib.auth.models import AbstractUser
from django.db import models

from core.jwt import jwt_encode


class User(AbstractUser):
    """
    User entity.
    """
    email = models.EmailField(unique=True)

    friends = models.ManyToManyField(
        'User', blank=True,
    )

    @property
    def jwt_token(self) -> str:
        payload = {'id': self.pk}
        return jwt_encode(payload)
    
    def add_friend(self, user: 'User'):
        self.friends.add(user)

    def remove_friends(self, user: 'User'):
        self.friends.remove(user)

    def is_friend(self, user: 'User') -> bool:
        return user in self.friends.all()
