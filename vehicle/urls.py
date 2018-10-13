from django.conf.urls import url
from vehicle.views import (vehicles, thar, time, 
			   vehicle_create_check, vehicle_update_check,vehicle_info)

app_name = "vehicles"

urlpatterns = [
    url(r'^$', vehicles, name="vehicles"),
    url(r'^1/$', thar, name="vehicle1"),
    url(r'^2/$', time, name="vehicle2"),
    url(r'^(?P<pk>\d+)/create/$', vehicle_create_check, name="vehicle_create_check"),
    url(r'^(?P<pk>\d+)/update/$', vehicle_update_check, name="vehicle_update_check"),
    url(r'^vehicle_info/$', vehicle_info, name="vehicle_info"),

]
