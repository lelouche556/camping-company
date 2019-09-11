from django.conf.urls import url
from destination import views

app_name = "destination"

urlpatterns = [
    url(r'^$', views.destination, name="destinations"),
    url(r'^(?P<slug>[\w-]+)/$', views.destination_detail_page, name="destination_detail_page"),
    # url(r'some/$', views.destination_detail_page, name="destination_detail_page"),

]
