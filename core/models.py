from pyclbr import Class
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    User_Identity = models.CharField(max_length=100)
    Flags = models.CharField(max_length=10)
    Utterance = models.TextField()
    Category = models.CharField(max_length=10)
    Intent = models.CharField(max_length=10)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField()
    class Meta:
        unique_together = ('email', 'role')
