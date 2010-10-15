#coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from youtube_search.forms import SearchForm


def search(request):
    context = RequestContext(request, {'form': SearchForm()})

    return render_to_response('search.html', context)

def do_search(request):
    search_url = 'http://www.youtube.com/results?search_query=%s&aq=f'

    form = SearchForm(request.POST)
    if form.is_valid():
        search_term = unicode(form.cleaned_data['full_text'] + ' cover')
        context = RequestContext(request, {'videos':[]})

        return render_to_response('search.html', context)
    else:
        context = RequestContext(request, {'form': form})

        return render_to_response('search.html', context)
