from django.conf.urls import url
from blog.views import all_blog, blog_detail

app_name = "blog"

urlpatterns = [
    url(r'^all/$', all_blog, name="all_blog"),
    url(r'^(?P<pk>\d+)/detail/$', blog_detail, name="blog_detail"),

]
