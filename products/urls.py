from django.contrib import admin
from django.urls import path, include
from .views import Navigation, ProductsViews, ProductsDetail

app_name = "products"
urlpatterns = [ 
    path('<str:slug>/', Navigation.as_view(), name='navigation'),
    path('collections/caskets/', ProductsViews.as_view(), name='collections'),
    path('<str:slug>/details/', ProductsDetail.as_view(), name='product-detail'),   
    path('collections/caskets/products/<str:slug>/', ProductsDetail.as_view(), name='collection-product-detail'),   
]

