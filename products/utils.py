import random
import string
from django.utils.text import slugify
import uuid

def images_directory_path(instance, filename):
    if (instance.__class__.__name__).lower() == 'image':
        return '/'.join(['upload', str(instance.item.__class__.__name__).lower(), str(instance.__class__.__name__).lower(), 
                        str(instance.item.name).replace('"', ''),
                        str(uuid.uuid4().hex + ".png")])
    else:    
        ext = filename.split(".")[-1]
        return '/'.join(['upload', str(instance.item.__class__.__name__).lower(), str(instance.__class__.__name__).lower(), 
                        str(instance.item.name).replace('"', ''), 
                        str(uuid.uuid4().hex + "." + ext)])

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug