from django import template
from ..models import Product

register = template.Library()


@register.filter
def uah(value):
    return f"{value} грн"


@register.simple_tag
def catalog_count():
    return Product.objects.count()