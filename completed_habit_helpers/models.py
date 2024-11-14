from django.db import models

# Create your models here.


class Completed_Habit_Helper(models.Model):
    habit_helper = models.ForeignKey(
        to = 'habit_helpers.Habit_Helper',
        related_name = 'completed_habits',
        on_delete = models.CASCADE
        )
    completed = models.DateTimeField(auto_now=True)
