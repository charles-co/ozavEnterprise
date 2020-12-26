"""ozav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Home
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns  = [
        url(r'^password/change/$', 
                auth_views.PasswordChangeView.as_view(), 
                name='password_change'),
        url(r'^password/change/done/$',
                auth_views.PasswordChangeDoneView.as_view(), 
                name='password_change_done'),
        url(r'^password/reset/$', 
                auth_views.PasswordResetView.as_view(), 
                name='password_reset'),
        url(r'^password/reset/done/$', 
                auth_views.PasswordResetDoneView.as_view(), 
                name='password_reset_done'),
        url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
                auth_views.PasswordResetConfirmView.as_view(), 
                name='password_reset_confirm'),
        url(r'^password/reset/complete/$', 
                auth_views.PasswordResetCompleteView.as_view(), 
                name='password_reset_complete'),
]

urlpatterns += [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('administration/', admin.site.urls),
    # path('products/', include('products.urls')),
    path('', Home.as_view(), name='index'),
    path('', include('pagedown.urls')),
    path('', include('products.urls')),
    path('', include('events.urls')),
]

handler404 = 'ozav.views.handler400'
handler500 = 'ozav.views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
