from django.conf.urls import url
from equipment.views import equipment_create_check, equipment_update_check

app_name = "equipment"

urlpatterns = [
    url(r'^(?P<pk>\d+)/create/$', equipment_create_check, name="equipment_create_check"),
    url(r'^(?P<pk>\d+)/update/$', equipment_update_check, name="equipment_update_check"),

]
