from django.db import models
import uuid
from django.conf import settings
from django.core.exceptions import ValidationError

MAX_COMMENT_DEPTH = 15

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='replies'
    )
    content = models.TextField()
    depth = models.PositiveIntegerField(default=0)
    is_removed = models.BooleanField(default=False)
    removed_reason = models.TextField(blank=True, null=True)
    edited_at = models.DateTimeField(blank=True, null=True)
    vote_count = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.parent:
            if self.parent.depth >= MAX_COMMENT_DEPTH:
                raise ValidationError(f'Maximum comment depth of {MAX_COMMENT_DEPTH} reached')
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'