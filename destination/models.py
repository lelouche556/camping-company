from django.db import models

# Create your models here.


class Destination(models.Model):
    place = models.CharField(max_length=64)
    description = models.TextField()
    activities = models.TextField()
    distance = models.IntegerField()
    hours = models.IntegerField()
    images = models.ImageField(upload_to='destination', blank=True)

    def __str__(self):
        return self.place
