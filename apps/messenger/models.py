from django.db import models
from accounts.models import User


class Message(models.Model):
    initialized_between = models.CharField(
        max_length=250, verbose_name="Initialized between"
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Sender", related_name="sender"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Receiver", related_name="receiver"
    )
    body = models.TextField(verbose_name="Body")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"New message from {self.receiver.first_name} {self.receiver.last_name} to {self.sender.first_name} {self.sender.last_name}"
