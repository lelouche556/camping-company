from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class VehicleCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="vehicle_check",
                             null=True, blank=True)
    engine_oil_level = models.PositiveIntegerField()
    brake_fluid_level = models.PositiveIntegerField()
    water_level = models.PositiveIntegerField()
    windscreen_washer = models.BooleanField()
    seatbelts_check = models.BooleanField()
    parking_brake = models.BooleanField()
    clutch_gearshift = models.BooleanField()
    burning_smell = models.BooleanField()
    steering_alignment = models.BooleanField()
    dashboard = models.BooleanField()
    check_lights = models.BooleanField()
    horn = models.BooleanField()
    tyres = models.BooleanField()
    leakage = models.BooleanField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
