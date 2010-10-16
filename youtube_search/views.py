# coding:utf-8
from xml.dom import minidom
import re
import gdata.youtube
import gdata.youtube.service

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from youtube_search.forms import SearchForm
from config_constants import *


def search(request):
    context = RequestContext(request, {'form': SearchForm()})

    return render_to_response('search.html', context)

def do_search(request):
    search_url = 'http://www.youtube.com/results?search_query=%s&aq=f'

    form = SearchForm(request.POST)
    if form.is_valid():
        search_term = form.cleaned_data['full_text'] + ' cover'
        results = __search_videos(search_term)

        context = RequestContext(request, {'videos':results})
        return render_to_response('search.html', context)

    else:
        context = RequestContext(request, {'form': form})

        return render_to_response('search.html', context)

def __search_videos(search_terms):
    '''
    Return a list of id videos found with the search_terms
    '''
    yt_service = gdata.youtube.service.YouTubeService()

    # The YouTube API does not currently support HTTPS/SSL access.
    yt_service.ssl = False

    yt_service.developer_key = DEVELOPER_KEY
    yt_service.client_id = CLIENT_ID

    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = search_terms
    query.orderby = 'viewCount'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)

    id_videos = []

    for entry in feed.entry:
        if entry.GetSwfUrl():
            regex_result = re.search('^.*v\/([^?]+)', entry.GetSwfUrl())
            id_videos.append({'title':entry.media.title.text.strip(), 'id':regex_result.group(1)})
    return id_videos
