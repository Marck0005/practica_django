from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Create your views here.
def about(request):
    return render(request, 'about.html')

# Create your views here.
def cruises(request):
    all_cruises = models.Cruise.objects.all()
    return render(request, 'cruises.html', {'cruises': all_cruises})# Create your views here.

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = "destination_detail.html"
    model = models.Destination
    contex_object_name = 'destination'

class DestinationCreateView(generic.CreateView):
    model = models.Destination
    template_name = "destination_form.html"
    fields = ['name','code_dest','description']

class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    template_name = "destination_form.html"
    fields = ['name','code_dest','description']


class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = "destination_confirm_delete.html"
    success_url = reverse_lazy('destinations')


