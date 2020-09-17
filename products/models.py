from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from .utils import images_directory_path
from .fields import OrderField
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
# Create your models here.

class Menu(MPTTModel):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50, db_index=True, editable=False, allow_unicode=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', db_index=True)
    is_active = models.BooleanField(default=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('slug', 'parent',)
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('blog:navigation',args=[self.slug])
        
    def __str__(self):
        return self.name

class ItemBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in':('product','event')})
    object_id= models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['object_id']
        abstract = True
        
    def render(self):
        return render_to_string('products/content/{}.html'.format(self._meta.model_name), {'item': self})

    def __str__(self):
        return self.item.name

class Image(ItemBase):
    file = models.ImageField(upload_to=images_directory_path)
    
class Video(ItemBase):
    url = models.URLField()

class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=70, db_index=True, unique=True, allow_unicode=True, editable=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = GenericRelation(Image, related_query_name="product_images")
    
    tags = TaggableManager()
    
    class Meta:
        ordering = ('created', 'updated')
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
         return reverse('products:product-detail',args=[self.slug])
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
    
    def get_markdown(self):
        return mark_safe(markdown(self.description))

    def __str__(self):
        return self.name
    
