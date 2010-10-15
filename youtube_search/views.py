# coding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from youtube_search.forms import SearchForm

import gdata.youtube
import gdata.youtube.service
from xml.dom import minidom
import re


def search(request):
    context = RequestContext(request, {'form': SearchForm()})

    return render_to_response('search.html', context)

def do_search(request):
    search_url = 'http://www.youtube.com/results?search_query=%s&aq=f'

    form = SearchForm(request.POST)
    if form.is_valid():
        youtube_url = search_url % (form.cleaned_data['full_text'] + '+cover')
        return HttpResponseRedirect(youtube_url)
    else:
        context = RequestContext(request, {'form': form})

        return render_to_response('search.html', context)

def search_video(search_terms):

    yt_service = gdata.youtube.service.YouTubeService()

    # The YouTube API does not currently support HTTPS/SSL access.
    yt_service.ssl = False

    yt_service.developer_key = 'AI39si68dTO_CHSQaYNalWbwLpFk3kGl14BsKeSrHNiC-n1FttkRBzpAHzkz77pKNdaZMa9s1lispwHXA1XSLJE8g8VgqI2X2Q'
    yt_service.client_id = 'youcover'

    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = search_terms
    query.orderby = 'viewCount'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)

    resultados = []
    for entry in feed.entry:
        m = re.search('^.*v\/([^?]+)', entry.GetSwfUrl())
        resultados.append((entry.media.title.text, m.group(1)))
    
    return resultados

