from django.contrib.auth.models import AbstractUser
from django.db import models


ROLES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user',
        verbose_name='Роль'
    )

    def __str__(self):
        return self.username
