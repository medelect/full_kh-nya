from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.http import HttpResponse
from .models import Dog
from django.views.generic.base import View 
from .forms import NameForm, MyForm, MyForm2
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

def myview2(request):

    if request.method == 'POST':
        form = MyForm2(request.POST, extra=request.POST.get('total_input_fields'))

        if form.is_valid():
            print "valid!"
    else:
        form = MyForm2()
    return render(request, "./soters/template2.html", { 'form': form })
