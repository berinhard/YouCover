#coding: utf-8

from django import forms

class SearchForm(forms.Form):
   full_text = forms.CharField(max_length=40, required = True, label = u'Artist: ')
