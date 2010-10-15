from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    url(r'', include('youtube_search.urls')),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
)
