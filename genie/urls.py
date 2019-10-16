from django.conf.urls import url
from django.urls import path
from genie.views import create,detail

app_name = "genie"

urlpatterns = [
           url('creation/', create, name='create'),
           # path('displaying/', display , name='display'),
           path('detail/', detail , name='detail')

       ]
