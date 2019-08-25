from django.conf.urls import url
from register.views import (signup, signin, sign_out, welcome)


app_name = "register"

urlpatterns = [
    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', signin, name="signin"),
    url(r'^logout/$', sign_out, name="signout"),
    url(r'^welcome/$', welcome, name="welcome"),
]
