from django.db import models

class CommunityType(models.TextChoices):
    PUBLIC = 'public', 'Public'
    RESTRICTED = 'restricted', 'Restricted'
    PRIVATE = 'private', 'Private'

class MembershipRole(models.TextChoices):
    MEMBER = 'member', 'Member'
    MODERATOR = 'moderator', 'Moderator'
    ADMIN = 'admin', 'Admin'

class PostType(models.TextChoices):
    TEXT = 'text', 'Text'
    IMAGE = 'image', 'Image'
    GALLERY = 'gallery', 'Gallery'
    VIDEO = 'video', 'Video'
    LINK = 'link', 'Link'

class MediaType(models.TextChoices):
    IMAGE = 'image', 'Image'
    VIDEO = 'video', 'Video'

class NotificationType(models.TextChoices):
    COMMENT_ON_POST = 'comment_on_post', 'Comment on Post'
    REPLY_TO_COMMENT = 'reply_to_comment', 'Reply to Comment'
    UPVOTE_POST = 'upvote_post', 'Upvote on Post'
    UPVOTE_COMMENT = 'upvote_comment', 'Upvote on Comment'
    NEW_POST_IN_COMMUNITY = 'new_post', 'New Post in Community'
    MENTION = 'mention', 'Mention'
    MOD_ACTION = 'mod_action', 'Moderator Action'
    BAN = 'ban', 'Ban'