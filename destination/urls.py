from django.conf.urls import url
from destination.views import destination,destination_detail_page,circuits

app_name = "destination"

urlpatterns = [
    url(r'^$', destination, name="destinations"),
    url(r'circuits/$', circuits, name="circuits"),
    url(r'^(?P<slug>[\w-]+)/$', destination_detail_page, name="destination_detail_page"),
]
