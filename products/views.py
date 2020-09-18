from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail, send_mass_mail
from django.db.models import Count
from django.core.cache import cache
from products.models import Product
from products.forms import ContactPostForm
# Create your views here.

class ProductsViews(ListView):
    model = Product
    paginate_by = 6
    paginate_orphans = 2
    template_name = 'products/product_list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()   
        return qs.filter(available=True).order_by('created')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub'] = "Caskets"
        return context

class ProductsDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product_tags_ids = self.object.tags.values_list('id', flat=True)
        similar_products = Product.objects.filter(tags__in=product_tags_ids).exclude(id=self.object.id)
        similar_products = similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags','-created')
        context["similiar_products"] = similar_products
        return context


class Navigation(View):
    
    def get(self, request, *args, **kwargs):

        if self.kwargs['slug'] == 'about':
            return render(request, 'about.html', {})

        elif self.kwargs['slug'] == 'contact-us':
            return redirect('products:contact-us')

        elif self.kwargs['slug'] == 'caskets':
            return redirect('products:collections')

        elif self.kwargs['slug'] == 'services':
            return render(request, 'services.html', {})

        elif self.kwargs['slug'] == 'events':
            return redirect('events:event-list')

class Contact(FormView):
    form_class = ContactPostForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('products:contact-us')

    def form_valid(self, form):
        cd = form.cleaned_data
        subject = 'Feedback from {} <{}>'.format(cd['name'], cd['email'])
        html_message = render_to_string('contact_us/email_template.html', {'email': cd['email'], 'name': cd['name'], 'message': cd['message'], 'phone': cd['phone_number']})
        message = 'Message' + '-'*30 + '\n\n{}'.format(cd["message"])
        sent = send_mail(subject, message, 'ch4rles.co@gmail.com', ['charlesboy49@gmail.com'], html_message=html_message, fail_silently=False)
        if sent:
            messages.success(self.request, "<strong>Hi {} !</strong> Your mail has been sent successfully, thank you.".format(cd['name']))
        return super(Contact, self).form_valid(form)

