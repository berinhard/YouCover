#coding: utf-8
from django.conf.urls.defaults import *

from shortcuts import route
from youtube_search.views import search, do_search

urlpatterns = patterns('',
    route(r'^$', GET=search, POST=do_search, name='search'),
)
