import uuid

from django.db import models

from shreadit.models.choices import CommunityType
from shreadit_backend import settings


class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    handle = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    banner = models.ImageField(upload_to='community/banners/', null=True, blank=True)
    icon = models.ImageField(upload_to='community/icons/', null=True, blank=True)
    visibility_type = models.CharField(
        max_length=10,
        choices=CommunityType.choices,
        default=CommunityType.PUBLIC
    )
    nsfw = models.BooleanField(default=False)
    member_count = models.IntegerField(default=0)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_communities',
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'communities'

    def __str__(self):
        return self.name