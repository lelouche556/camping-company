from django.conf.urls import url
from destination.views import (destination, destination_detail_page,
                               circuits, circuit,success)

app_name = "destination"

urlpatterns = [
    url(r'^$', destination, name="destinations"),
    url(r'circuits/$', circuits, name="circuits"),
    url(r'success/$', success, name="success"),
    url(r'^(?P<slug>[\w-]+)/$', destination_detail_page, name="destination_detail_page"),
    url(r'^circuits/(?P<slug>[\w-]+)/$', circuit, name="circuit"),
]