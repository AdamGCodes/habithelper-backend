from django.db import models

# Create your models here.
class Journal(models.Model):
    text = models.TextField(blank=True, null=False)
    author = models.ForeignKey(
        to='users.User',
        related_name='user_journals',
        on_delete=models.CASCADE
    )