from django.conf.urls import url
from register.views import (signup, signin, sign_out,
                            welcome, pass_reset,pass_rediretor)


app_name = "register"

urlpatterns = [
    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', signin, name="signin"),
    url(r'^logout/$', sign_out, name="signout"),
    url(r'^welcome/$', welcome, name="welcome"),
    url(r'^reset/(?P<slug>[\w-]+)/$', pass_rediretor, name="pass_rediretor"),
    url(r'^reset/$', pass_reset, name="pass_reset"),

]
