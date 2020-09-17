from django.contrib import admin
from django.urls import path, include
from .views import Navigation, ProductsViews, ProductsDetail, Contact

app_name = "products"
urlpatterns = [
    path('contact-us/', Contact.as_view(), name='contact-us'), 
    path('<str:slug>/', Navigation.as_view(), name='navigation'),
    path('collections/caskets/', ProductsViews.as_view(), name='collections'),
    path('collections/caskets/products/<str:slug>/', ProductsDetail.as_view(), name='product-detail'),   
]

