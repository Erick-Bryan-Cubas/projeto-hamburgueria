from django import template

register = template.Library()

@register.filter
def discounted_price(product, quantity):
    if product.discount:
        return product.price * quantity * (1 - product.discount / 100)
    return product.price * quantity
