from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EquipmentCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="equipment_check")
    yellow_box = models.BooleanField()
    kettel = models.BooleanField()
    utensils = models.BooleanField()
    stove = models.BooleanField()
    bbq_grill = models.BooleanField()
    spare_tyre = models.BooleanField()
    shovel = models.BooleanField()
    mug_bucket = models.BooleanField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inventory")
    degree_8_sleeping = models.IntegerField(blank=True)
    degree_summer_sleeping = models.IntegerField(blank=True)
    kettle = models.IntegerField(blank=True)
    stove = models.IntegerField(blank=True)
    plates = models.IntegerField(blank=True)
    ground_tent = models.IntegerField(blank=True)
    charger = models.IntegerField(blank=True)
    chairs = models.IntegerField(blank=True)
    foldable_table_and_chair = models.IntegerField(blank=True)
    canister = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
