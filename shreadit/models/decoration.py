import uuid
from django.db import models
from django.conf import settings

class Decoration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='decorations'
    )
    community = models.ForeignKey(
        'Community',  # was pointing to AUTH_USER_MODEL
        on_delete=models.CASCADE,
        related_name='decorations'
    )
    color = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserDecoration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_decorations'
    )
    community = models.ForeignKey(
        'Community',  # needed to scope flair to a community
        on_delete=models.CASCADE,
        related_name='user_decorations'
    )
    decoration = models.ForeignKey(
        'Decoration',  # was pointing to AUTH_USER_MODEL
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_decorations'
    )
    custom_txt = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')


class PostDecoration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    decoration = models.ForeignKey(
        'Decoration',  # was pointing to AUTH_USER_MODEL
        on_delete=models.CASCADE,
        related_name='post_decorations'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='decorations'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'decoration')