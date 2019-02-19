from django.contrib import admin
from vehicle.models import VehicleCheck, VehicleDefinition

# Register your models here.

admin.site.register(VehicleCheck)
admin.site.register(VehicleDefinition)