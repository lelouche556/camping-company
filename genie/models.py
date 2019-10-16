from django.db import models
from django.contrib.auth.models import User
from vehicle.models import Book

# Create your models here.
class mainFrame(models.Model):
	object_id= models.ForeignKey(Book, on_delete=models.CASCADE)
	front_image = models.ImageField(upload_to="genie/mainframe", blank=True, null=True)
	back_image = models.ImageField(upload_to="genie/mainframe", blank=True, null=True)
	left_image = models.ImageField(upload_to="genie/mainframe", blank=True, null=True)
	right_image = models.ImageField(upload_to="genie/mainframe", blank=True, null=True)

	def __str__(self):
		return self.object_id

class vehicleCleanliness(models.Model):
	object_id= models.ForeignKey(Book, on_delete=models.CASCADE)
	first_image = models.ImageField(upload_to="genie/cleanliness", blank=True, null=True)
	second_image = models.ImageField(upload_to="genie/cleanliness", blank=True, null=True)
	third_image = models.ImageField(upload_to="genie/cleanliness", blank=True, null=True)
	fourth_image = models.ImageField(upload_to="genie/cleanliness", blank=True, null=True)

	def __str__(self):
		return self.object_id

class photos(models.Model):
	object_id= models.ForeignKey(Book, on_delete=models.CASCADE)
	first_image = models.ImageField(upload_to="genie/photo", blank=True, null=True)
	second_image = models.ImageField(upload_to="genie/photo", blank=True, null=True)

	def __str__(self):
		return self.object_id

