from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.http import HttpResponse
from .models import Dog
from django.views.generic.base import View 
from .forms import NameForm, MyForm
#import dynaform

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DogView(generic.ListView): 
    template_name = 'soters/dog_tmpl.html'
    context_object_name = 'DogList'

    def get_queryset(self):
        return Dog.objects.all()

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
        return render(request, './soters/name.html', {'form': form})

def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print "valid!"
    else:
            form = MyForm()
    return render(request, "./soters/template.html", { 'form': form })

def dform(request):
    json_form = get_json_form_from_somewhere()
    form_class = dynaform.get_form(json_form)
    data = {}
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form = form_class()

    return render_to_response( "dform.html", {'form': form, 'data': data,}, RequestContext(request))
