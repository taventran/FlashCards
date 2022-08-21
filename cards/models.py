from django.db import models
from django.conf import settings

class Set(models.Model):
    setName = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.setName

class Card(models.Model):
    term = models.TextField(max_length=500)
    definition = models.TextField(max_length=2000)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='cards')


    def __str__(self):
        return self.term[0:15]

