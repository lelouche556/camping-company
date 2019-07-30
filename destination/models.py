from django.db import models
from django.db.models.signals import pre_save

# Create your models here.

# All Destination


class Destination(models.Model):
    place = models.CharField(max_length=64)
    description = models.TextField()
    distance = models.IntegerField()
    hours = models.IntegerField()
    accommodation = models.CharField(max_length=64)
    important_to_know = models.CharField(max_length=128)
    night_time_temperature_summer = models.CharField(max_length=64)
    night_time_temperature_winter = models.CharField(max_length=64)
    season = models.CharField(max_length=64)
    slug = models.SlugField(max_length=40, blank=True, null=True)
    #location and known for

    def __str__(self):
        return self.place

# Detail map location model


class Image(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='maps/detail', blank=True)
    image2 = models.ImageField(upload_to='maps/detail', blank=True)
    image3 = models.ImageField(upload_to='maps/detail', blank=True)
    image4 = models.ImageField(upload_to='maps/detail', blank=True)

    def __str__(self):
        return self.destination.place


class Amenity(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    basic_toilet = models.CharField(max_length=64, default="No")
    bathroom = models.CharField(max_length=64, default="No")
    kitchen = models.CharField(max_length=64, default="No")
    pets_allowed = models.CharField(max_length=64, default="No")
    charging_points = models.CharField(max_length=64, default="No")
    drinking_water = models.CharField(max_length=64, default="No")
    covered_area = models.CharField(max_length=64, default="No")
    barbeque_grills = models.CharField(max_length=64, default="No")
    good_for_groups = models.CharField(max_length=64, default="No")
    campfire = models.CharField(max_length=64, default="No")
    picnic_table = models.CharField(max_length=64, default="No")
    breakfast = models.CharField(max_length=64, default="No")

    def __str__(self):
        return self.destination.place


class Detail(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    type_of_land = models.CharField(max_length=64)
    accessible_By = models.CharField(max_length=64)
    check_in = models.CharField(max_length=64)
    check_out = models.CharField(max_length=64)
    cancellation_policy = models.CharField(max_length=64)

    def __str__(self):
        return self.destination.place


class Activity(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    off_roading = models.CharField(max_length=64, default="No")
    trekking = models.CharField(max_length=64, default="No")
    boating = models.CharField(max_length=64, default="No")

    def __str__(self):
        return self.destination.place

# map related


class Map(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=128, blank=True, null=True)
    longitude = models.FloatField(max_length=128, blank=True, null=True)
    images = models.ImageField(upload_to='maps/image', blank=True)
    iconImage = models.ImageField(upload_to='maps/iconImage', blank=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.destination.place


class Region(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    region = models.ManyToManyField(Map, related_name="Region")
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


def destination_pre_save_receiver(sender, instance, **kwargs):
    title = instance.place.split()
    instance.slug = "-".join(title).replace("?", "")
    # slug cant have question marks boy


pre_save.connect(destination_pre_save_receiver, sender=Destination)