import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.username