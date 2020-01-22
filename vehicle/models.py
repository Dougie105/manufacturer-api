from django.db import models
from django.contrib.auth.models import User

class Maserati(models.Model):
    year = models.IntegerField(blank=False)
    model = models.CharField(max_length=20)
    description = models.TextField()
    recieved = models.DateTimeField(auto_now_add=True)
    updated = models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.model