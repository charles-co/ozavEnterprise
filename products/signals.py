from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.utils import unique_slug_generator
from products.models import Menu, Product

@receiver(pre_save, sender=Menu)
def menu_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=Product)
def product_pre_save_receiver(sender, instance, **kwargs):
        instance.slug = unique_slug_generator(instance)