from django import template


# Creating customs tags and filters on Django documentation
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
