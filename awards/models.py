from django.db import models

# Create your models here.


class Award(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True) #Need to unnullify when comes to using them
    condition = models.CharField(max_length=200, null=True)
    image = models.URLField(null=True)

