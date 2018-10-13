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
