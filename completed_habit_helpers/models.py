from django.db import models

# Create your models here.

#???????????????? Do I need to popopulate with user and call reference in the serializer?
class Completed_Habit_Helper(models.Model):
    habit_helper = models.ForeignKey(
        to = 'habit_helpers.Habit_Helper',
        related_name = 'completed_habits',
        on_delete = models.CASCADE
        )
    completed = models.DateTimeField(auto_now_add=True)
