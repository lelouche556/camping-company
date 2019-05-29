from django.conf.urls import url
from payment.views import (cart, checkout,
                           payment_success,
                           payment_failure,
                           )

app_name = "payment"

urlpatterns = [
    url(r'^$', cart, name="payment"),
    url(r'^checkout/$', checkout, name="checkout"),
    url(r'^success/$', payment_success, name="success"),
    url(r'^failure/$', payment_failure, name="failure"),
]