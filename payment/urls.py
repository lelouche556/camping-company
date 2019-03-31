from django.conf.urls import url
from payment.views import add_card

app_name = "payment"

urlpatterns = [
    url(r'^$', add_card, name="add_card"),
]
