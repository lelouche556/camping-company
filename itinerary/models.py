from django.db import models
from django.contrib.auth.models import User
from destination.models import Destination
# Create your models here.


class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="itinerary_check")
    destination = models.ManyToManyField(Destination, blank=True, related_name="trips")
    created_time = models.TimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
