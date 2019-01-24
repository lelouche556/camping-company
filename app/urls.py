from django.conf.urls import url
from app import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^findus/$', views.findus, name="findus"),
    url(r'^destinations/$', views.destination, name="destination"),
    url(r'^represent/$', views.represent, name="represent"),
    url(r'^calender/$', views.calender, name="calender"),
    url(r'^find/user/$', views.find_user, name="find_user"),
    url(r'^status/(?P<pk>\d+)/show/$', views.show_status, name="show_status"),
    url(r'^status/(?P<pk>\d+)/create/$', views.create_status, name="create_status"),
    url(r'^terms_condition/$', views.terms_condition, name="terms_condition"),
    url(r'^faq/$', views.faq, name="faq"),
    url(r'^all_user/$', views.all_user, name="all_user"),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),

]
