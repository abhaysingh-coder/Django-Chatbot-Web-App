from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    Flags = models.CharField(max_length=10),
    Utterance = models.TextField(),
    Category = models.CharField(max_length=10),
    Intent = models.CharField(max_length=10)
