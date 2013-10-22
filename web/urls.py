from django.conf.urls import patterns
from web.views import shorten


urlpatterns = patterns('',
       (r'^shorten$', shorten),
)