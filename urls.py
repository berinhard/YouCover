from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'', include('youtube_search.urls')),
)
