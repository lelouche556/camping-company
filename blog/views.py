from django.shortcuts import render
from blog.models import Blog
import datetime

# Create your views here.


def all_blog(request):
    blogs = Blog.objects.all().order_by("-created_time")
    return render(request, "blog/all_blog.html", {"all": blogs})


def blog_detail(request, pk):
    author = Blog.objects.get(pk=pk)
    return render(request, "blog/detail.html", {"author": author})


def create_blog(request):
    return render(request, "blog/create.html")