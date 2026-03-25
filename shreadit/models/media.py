from django.db import models
import uuid
from django.conf import settings
from .choices import MediaType

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='media'
    )
    media_type = models.CharField(
        max_length=5,
        choices=MediaType.choices,
        default=MediaType.IMAGE
    )
    file = models.FileField(upload_to='posts/media/')
    url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    size = models.PositiveIntegerField()
    mime_type = models.CharField(max_length=50)
    is_processed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.post.title} — {self.media_type} ({self.order})'