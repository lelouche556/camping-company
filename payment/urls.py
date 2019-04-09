from django.conf.urls import url
from payment.views import cart, checkout

app_name = "payment"

urlpatterns = [
    url(r'^$', cart, name="payment"),
    url(r'^checkout/$', checkout, name="checkout"),
]
