from django.db import models
from user.models import User


class MessengerPolicy(models.Model):
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='sender')
    reciever = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='reciever')
    block_by_sender = models.BooleanField(default=False)
    block_by_reciever = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'reciever')


class MessageList(models.Model):
    policy = models.ForeignKey(MessengerPolicy,
                               on_delete=models.CASCADE,
                               related_name="messages")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
