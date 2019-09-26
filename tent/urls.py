from django.conf.urls import url
from tent.views import tent_create_check, tent_update_check

app_name = "tent_check"

urlpatterns = [
    url(r'^(?P<pk>\d+)/create/$', tent_create_check, name="tent_create_check"),
    url(r'^(?P<pk>\d+)/update/$', tent_update_check, name="tent_update_check"),

]