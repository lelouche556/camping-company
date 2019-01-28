from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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


def save1(trip, vehicle, tent, equipment, itinerary):
    if trip.trip_status == "Ended":
        trip.active = False
        vehicle.active = False
        tent.active = False
        equipment.active = False
        itinerary.active = False

        trip.save()
        vehicle.save()
        tent.save()
        equipment.save()
        itinerary.save()

    # if trip.trip_status == "ongoing":
    #     trip.active = True
    #     vehicle.active = True
    #     tent.active = True
    #     equipment.active = True
    #     itinerary.active = True
    #
    #     trip.save()
    #     vehicle.save()
    #     tent.save()
    #     equipment.save()
    #     itinerary.save()


def my_post_save_handler(sender, instance, **kwargs):
    post_save.disconnect(my_post_save_handler, sender=sender)
    trip = instance
    user = User.objects.get(username=trip.user.username)
    trip = user.trip_check.get(user=user, active=True)
    vehicle = user.vehicle_check.get(user=user, active=True)
    tent = user.tent_check.get(user=user, active=True)# active=True
    equipment = user.equipment_check.get(user=user, active=True)
    itinerary = user.itinerary_check.get(user=user, active=True)
    save1(trip, vehicle, tent, equipment, itinerary)

    post_save.connect(my_post_save_handler, sender=sender)


post_save.connect(my_post_save_handler, sender=Trip)