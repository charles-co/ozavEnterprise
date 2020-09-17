from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from products.utils import images_directory_path
from taggit.managers import TaggableManager
from products.models import Image, Video

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    image = GenericRelation(Image, related_query_name="event_images")
    video = GenericRelation(Video, related_query_name="event_videos")

    class Meta:
        ordering = ('created',)

    def render(self):
        return render_to_string('events/content/{}.html'.format(self._meta.model_name), {'item': self})

