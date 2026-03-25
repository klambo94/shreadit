import uuid

from django.db import models

from shreadit.models.choices import PostType
from shreadit_backend import settings


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    community = models.ForeignKey(
        'Community',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    post_type = models.CharField(
        max_length=10,
        choices=PostType.choices,
        default=PostType.TEXT
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    nsfw = models.BooleanField(default=False)
    spoiler = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    removed_reason = models.TextField(blank=True, null=True)
    vote_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    edited_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title