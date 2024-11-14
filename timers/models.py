from django.db import models

# Create your models here.
class Timer(models.Model):
    name = models.CharField(max_length=100, null=False)
    reason = models.CharField(max_length=200)
    started = models.DateTimeField(auto_now_add=True) #Front end will have option to select a date in the past or "Right now" button. Resetting the timer will add current timedate in here.
    exceptions = models.PositiveIntegerField() #Stretch goal allowing a number of free passes e.g. cutting down on smoking 3 would give 3 tick boxes or three "strikes" on the timer
    user = models.ForeignKey(
        to='users.User',
        related_name='user_timers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
