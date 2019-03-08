from django.db import models
from django.db.models.signals import pre_save

# Create your models here.


class Destination(models.Model):
    place = models.CharField(max_length=64)
    description = models.TextField()
    activities = models.TextField()
    distance = models.IntegerField()
    hours = models.IntegerField()
    images = models.ImageField(upload_to='destination', blank=True)
    slug = models.SlugField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.place


def destination_pre_save_receiver(sender, instance, **kwargs):
    title = instance.place.split()
    instance.slug = "-".join(title).replace("?", "")
    # slug cant have question marks boy


pre_save.connect(destination_pre_save_receiver, sender=Destination)