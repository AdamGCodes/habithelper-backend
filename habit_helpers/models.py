from django.db import models

# Create your models here.
class Habit_Helper(models.Model):
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=200, null=True)
    target = models.IntegerField()
    completed_count = models.IntegerField()
    user = models.ForeignKey(
        to='users.User',
        related_name='user_habit_helper',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
