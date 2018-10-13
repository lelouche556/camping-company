from django.conf.urls import url
from customer.views import (user_page, book,
                            itinerary_detail_page,
                            custom_itinerary,
                            create_itinerary,
                            delete_itinerary, trip_detail)

app_name = "customer"

urlpatterns = [
    url(r'^$', user_page, name="user_page"),
    url(r'^create/$', create_itinerary, name="create_itinerary"),
    url(r'^(?P<pk>\d+)/detail/$', itinerary_detail_page, name="itinerary_detail_page"),
    url(r'^book/(?P<pk>\d+)/success/$', book, name="book"),
    url(r'^itinerary/delete/$', delete_itinerary, name="delete_itinerary"),
    url(r'^itinerary/$', custom_itinerary, name="custom_itinerary"),
    url(r'^trip_detail/$', trip_detail, name="trip_detail"),

]
