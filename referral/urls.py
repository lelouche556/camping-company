from django.conf.urls import url
from referral.views import referred_view


app_name = "referral"

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', referred_view, name="referred"),
]
