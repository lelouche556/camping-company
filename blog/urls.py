from django.conf.urls import url
from blog.views import all_blog

app_name = "blog"

urlpatterns = [
    url(r'^all/$', all_blog, name="all_blog"),

]
