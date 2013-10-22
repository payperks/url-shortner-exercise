from django.conf.urls import patterns, include, url
from web.views import go


urlpatterns = patterns('',
    url(r'^web/', include('web.urls')),
   (r'^.*/?$', go),

)