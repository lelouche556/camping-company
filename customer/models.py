from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_check", null=True)
    phone = models.BigIntegerField()
    license_number = models.BigIntegerField()
    city = models.CharField(max_length=12)
    address = models.CharField(max_length=64)
    nickname = models.CharField(max_length=12)
    about = models.TextField()

    def __str__(self):
        return self.user.username
