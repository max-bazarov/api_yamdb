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
    confirmation_code = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.username
