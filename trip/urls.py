from django.conf.urls import url
from trip.views import trip_create, trip_update

app_name = "trip"

urlpatterns = [
    url(r'^(?P<pk>\d+)/create/$', trip_create, name="create_trip"),
    url(r'^(?P<pk>\d+)/update/$', trip_update, name="update_trip"),

]
