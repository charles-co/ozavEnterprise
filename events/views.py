from django.shortcuts import render
from .models import Event
from django.views.generic.list import ListView

# Create your views here.

class EventList(ListView):
    model = Event
    template_name = 'events/events.html'
    paginate_by = 10
    paginate_orphans = 4
