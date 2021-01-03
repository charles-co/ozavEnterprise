from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic import TemplateView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.utils.decorators import method_decorator
# from django.http import JsonResponse
# from django.apps import apps
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import modelform_factory
from django.db.models import Count
# from braces.views import JsonRequestResponseMixin, CsrfExemptMixin
# from django.core.cache import cache
from products.models import Product, Menu
from events.models import Event

class Home(TemplateView):
    template_name = 'index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            self.caskets = Product.objects.filter(available=True)[:10].prefetch_related("image").order_by('price')
            self.events = Event.objects.all()[:20].prefetch_related("image")
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caskets'] = self.caskets
        context['events'] = self.events
        return context

def handler404(request, exception):
    return render(request, 'error.html', {'error': '404', 'error_message': '404 Not Found'}, status=404)

def handler400(request, exception):
    return render(request, 'error.html', {'error': '400', 'error_message': '400 Bad Request'}, status=400)

def handler500(request):
    return render(request, 'error.html', {'error': '500', 'error_message': '500 Internal Server Error'}, status=500)       


    