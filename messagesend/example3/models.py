from django.db import models

class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender_name} to {self.recipient_name} - {self.timestamp}'
