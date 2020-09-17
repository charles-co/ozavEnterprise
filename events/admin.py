from django.contrib import admin
from .models import Event
from django.contrib.contenttypes.admin import GenericStackedInline
from products.models import Image, Video
# Register your models here.

class ImageInline(GenericStackedInline):
    model = Image
    extra = 1

class VideoInline(GenericStackedInline):
    model = Video
    extra = 1

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    inlines = [ImageInline, VideoInline]
    
    class Media:
       pass

admin.site.register(Event, EventAdmin)
# admin.register(Video)
# admin.register(Image)
