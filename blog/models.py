from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # maybe image upload in future
    # comments??
    # views/like??
    created_date = models.DateField(auto_now_add=True)
    created_time = models.DateField(auto_now_add=True)
