from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")
    txnid = models.CharField(max_length=128, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    productinfo = models.CharField(max_length=32, default='car book')
    phone = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
