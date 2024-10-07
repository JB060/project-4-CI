from django.db import models

# Create your models here.

class Room (models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DataTimeField(auto_now=True)
    created = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
