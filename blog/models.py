from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # heading = models.CharField(max_length=64)
    # sub_heading = models.CharField(max_length=64)
    # description = models.CharField(max_length=128)
    # content = models.TextField()
    # # tags = models.TextField() comments?? views/like??
    # blog_images = models.ImageField(upload_to="blog_images", blank=True)
    # blog_cover_images = models.ImageField(upload_to="blog_cover_images", blank=True)
    # created_date = models.DateField(auto_now_add=True)
    # created_time = models.TimeField(auto_now_add=True)
    # approved = models.BooleanField(default=False)
    content = models.TextField()
    created_date = models.DateField()
    created_time = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField()
    blog_cover_images = models.ImageField(upload_to="blog_cover_images", blank=True)

    def __str__(self):
        return self.user.username