from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    awards = models.ManyToManyField(
        to='awards.Award',
        related_name='users',
    )
    friends = models.ManyToManyField(
        to='users.User',
    )
    quotes = models.ManyToManyField(
        to='quotes.Quote',
        related_name='users',
    )
