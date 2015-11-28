from django.conf.urls import patterns, url
from api import views
# from pb.views import some class base views
from django.conf import settings


urlpatterns = patterns('',
        # show the bill info via Consumer Num
        url(r'bill_info/(?P<consumer_num>[0-9]+)/$', views.bill_info, name='bill_info'),)