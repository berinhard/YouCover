#coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

from youtube_search.forms import SearchForm


def search(request):
    context = RequestContext(request, {'form': SearchForm()})

    return render_to_response('search.html', context)
