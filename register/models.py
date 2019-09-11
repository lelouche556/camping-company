from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse


class Password(models.Model):
    email = models.EmailField(max_length=128)
    slug = models.SlugField(blank=True, unique=True)
    reset_link = models.CharField(max_length=64, blank=True, null=True)
    initiate_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.email


def referral_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.reset_link = "https://www.camping-co.com" + reverse("register:pass_reset") + instance.slug

pre_save.connect(referral_pre_save_receiver, sender=Password)
