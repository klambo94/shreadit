import uuid

from django.db import models

from shreadit.models import Community


class CommunityRule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    community = models.ForeignKey(Community,
                                  on_delete=models.CASCADE,
                                  related_name='rules')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('community', 'order')

    def __str__(self):
        return f'{self.community.name} — Rule {self.order}: {self.title}'
