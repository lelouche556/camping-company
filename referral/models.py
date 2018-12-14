from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .utils import unique_slug_generator


class Referral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referrer")
    slug = models.SlugField(blank=True, unique=True)
    referred_users = models.ManyToManyField(User, related_name="referred", blank=True)
    referred_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referred_by", blank=True, null=True)
    referred = models.BooleanField(default=False)
    referral_link = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.slug


def referral_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.referral_link = "https://www.camping-co.com/referral/referred/" + instance.slug


pre_save.connect(referral_pre_save_receiver, sender=Referral)
