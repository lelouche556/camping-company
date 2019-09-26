from django.conf.urls import url
from equipment.views import (equipment_create_check,
                             equipment_update_check,
                             inventory_create,
                             inventory_update)

app_name = "equipment"

urlpatterns = [
    url(r'^(?P<pk>\d+)/create/$', equipment_create_check, name="equipment_create_check"),
    url(r'^(?P<pk>\d+)/update/$', equipment_update_check, name="equipment_update_check"),
    url(r'^(?P<pk>\d+)/inventory_create/$', inventory_create, name="inventory_create"),
    url(r'^(?P<pk>\d+)/inventory_update/$', inventory_update, name="inventory_update"),

]
