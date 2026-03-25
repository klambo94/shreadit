import uuid

from django.db import models

from shreadit.models.choices import MembershipRole
from shreadit_backend import settings


class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    community = models.ForeignKey(
        'Community',
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    role = models.CharField(
        max_length=9,
        choices=MembershipRole.choices,
        default=MembershipRole.MEMBER
    )

    favorite = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    ban_reason = models.CharField(max_length=255, blank=True, null=True)
    ban_expires = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('member', 'community')