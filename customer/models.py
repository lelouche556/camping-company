from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_check", null=True)
    phone = models.BigIntegerField()
    license_number = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    nickname = models.CharField(max_length=64)
    about = models.TextField()
    terms_condition = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
