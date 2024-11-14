from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_set = models.CharField(max_length=50)
    quote = models.TextField(max_length=400)
    author = models.TextField(max_length=50)
