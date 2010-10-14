#coding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'youtube_search.views.search', name='search'),
)
