from django.conf.urls import url
from pay.views import (cart, payment_success, payment_failure)

app_name = "pay"

urlpatterns = [
    url(r'^$', cart, name="pay"),
    url(r'^success/$', payment_success, name="success"),
    url(r'^failure/$', payment_failure, name="failure"),
]