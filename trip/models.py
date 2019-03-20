from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from vehicle.models import VehicleDefinition

# Create your models here.

trip_status = (
    ("Ended", "Ended"),  # first pair is what save in db
    ("Ongoing", "Ongoing"),
    ("Upcoming", "Upcoming")
)

car_type = (
    ("Thar", "Thar"),
    ("Xenon 2014", "Xenon 2014"),
    ("Xenon 2018", "Xenon 2018")
)


class Trip (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trip_check")
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    duration_of_trip = models.PositiveIntegerField(blank=True, null=True)
    amount_paid = models.BigIntegerField(blank=True, null=True)
    destination = models.CharField(blank=True, max_length=128, null=True)
    residence_address = models.CharField(blank=True, max_length=128, null=True)
    trip_status = models.CharField(blank=True, max_length=128, null=True, choices=trip_status)
    car_type = models.CharField(blank=True, max_length=64, null=True, choices=car_type)
    active = models.BooleanField(default=True)
    guest = models.IntegerField()

    def __str__(self):
        return self.user.username


def trip_post_save_receiver(sender, instance, *args, **kwargs):
    vehicle = VehicleDefinition.objects.filter(car_name=instance.car_type)
    if vehicle.count() < 1:
        VehicleDefinition(check_in_date=instance.check_in_date,
                          check_out_date=instance.check_out_date,
                          car_name=instance.car_type).save()

post_save.connect(trip_post_save_receiver, sender=Trip)
