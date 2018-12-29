from django.shortcuts import render
from blog.models import Blog, Image

# Create your views here.


def all_blog(request):
    blogs = Blog.objects.all().order_by("-id")
    # try:
    #     blogs = Blog.objects.all().order_by("-created_time")
    # except Blog.DoesNotExist:
    #     blogs = None
    return render(request, "blog/all_blog.html", {"all": blogs})


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    # user = User.objects.get(pk=pk)
    image_ = Image.objects.filter(blog=blog).order_by("-id")
    # for x in image_:
    #     print(type(x.blog_image2.url))
    return render(request, "blog/detail.html", {"blog": blog, "image": image_})


def create_blog(request):
    return render(request, "blog/create.html")