from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
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
from django.core.cache import cache
from products.models import Product, Menu


class Home(ListView):
    model = Product
    paginate_by = 10
    paginate_orphans = 4
    template_name = 'index.html'
    
    def get_queryset(self):
        qs = super().get_queryset()   
        return qs.filter(available=True).order_by('created')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menus'] = self.menus
        return context

def handler404(request, exception):
    return render(request, 'error.html', {'error': '404', 'error_message': '404 Not Found'}, status=404)

def handler400(request, exception):
    return render(request, 'error.html', {'error': '400', 'error_message': '400 Bad Request'}, status=400)

def handler500(request):
    return render(request, 'error.html', {'error': '500', 'error_message': '500 Internal Server Error'}, status=500)       


    