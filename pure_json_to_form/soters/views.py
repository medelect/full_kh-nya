from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.http import HttpResponse
from .models import MyStore
from django.views.generic.base import View
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
import forms


def dform(request):
    json_form = get_json_form_from_somewhere()
    form_class = forms.get_form(json_form)
    data = {}
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form = form_class()

    return render_to_response( "dform.html", {'form': form,  'data': data,}, RequestContext(request) )

