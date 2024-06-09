# core/templatetags/cart_tags.py
from django import template
from core.models import Product

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return Product.objects.get(id=key)

@register.filter
def multiply(value, arg):
    return value * arg
