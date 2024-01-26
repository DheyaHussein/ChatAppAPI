from django.db import models

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)