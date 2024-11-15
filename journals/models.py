from django.db import models

# ???????????????? Do I need to popopulate with user and call reference in the serializer?
# Create your models here.
class Journal(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(
        to='users.User',
        related_name='user_journals',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
