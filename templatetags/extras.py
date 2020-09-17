from django import template
register = template.Library()

from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe
from products.models import Menu
from math import ceil
# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
# from django.contrib import messages
# from django.http import HttpResponseRedirect

# from blog.models import Post
# import logging
# logger = logging.getLogger(__name__)

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None

@register.filter
def currency(naira):
    if naira:
        naira = round(float(naira), 2)
        return mark_safe("&#8358;{}{}".format(intcomma(int(naira)), ("%0.2f" % naira)[-3:]))

@register.filter(is_safe=False)
def times(number):
    return range(ceil(number))

@register.filter(is_safe=False)
def divide(value, arg):
    """Divide the arg to the value."""
    try:
        return int(value) / int(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''

@register.filter(is_safe=False)
def mulp(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''

@register.inclusion_tag('tags/_menu_list.html', takes_context=True)
def navigation_list(context):
    menus = Menu.objects.filter(is_active=True)
    request = context['request']
    return {'menus': menus, 'request': request}

# @register.inclusion_tag('tags/_contact_us.html')
# def contact_us():
#     return {'form': EmailPostForm()}

# @register.inclusion_tag('tags/_side_bar.html')
# def side_bar():
#     posts = Post.objects.published()[:5]
#     return {'posts': posts}

# @register.inclusion_tag('tags/_subscriber.html')
# def subscribe():
#     return {'form': SubscribeForm()}    

# @register.inclusion_tag('tags/_carousel.html')
# def carousel(id):
#     post = Post.objects.get(id=id)
#     return{'post': post}
