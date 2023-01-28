from django.db import models
from common.models import CommonModel

class ChatRoom(CommonModel):
    """
    Chat Room Model Definition
    """
    users = models.ManyToManyField(
        "users.User",
        related_name="chatrooms",
    )

    def __str__(self) -> str:
        return "Chat Room"

class Message(CommonModel):
    """
    Message Model Definition
    """
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL, # if user deletes their account, messages persis
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE, # if the chatroom deleted, messages should be deleted
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"