from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=64)
    sub_heading = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    # tags = models.TextField() comments?? views/like??
    blog_images = models.ImageField(upload_to="blog_images", blank=True)
    blog_cover_images = models.ImageField(upload_to="blog_images", blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    blog_image1 = models.ImageField(upload_to="blog_image", blank=True)
    blog_image2 = models.ImageField(upload_to="blog_image", blank=True)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.blog.heading


class Form(models.Model):
    referral = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    driving = models.CharField(max_length=64)
    food = models.CharField(max_length=64)
    sleep = models.CharField(max_length=64)
    anything = models.CharField(max_length=64)

    def __str__(self):
        return self.email