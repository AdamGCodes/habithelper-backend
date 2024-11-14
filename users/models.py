from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    awards = models.ForeignKey(
        to='awards.Award',
        related_name='user_awards',
        on_delete=models.CASCADE
    )
    friends = models.ForeignKey(
        to='users.User',
        related_name='user_friends',
        on_delete=models.CASCADE
    )
    quotes = models.ForeignKey(
        to='quotes.Quote',
        on_delete=models.CASCADE
    )
