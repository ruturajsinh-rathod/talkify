from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    is_online = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = ['username']  # still require username on creation

    def __str__(self):
        return self.email
