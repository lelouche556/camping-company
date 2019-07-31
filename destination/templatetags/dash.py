from django import template

register = template.Library()


@register.filter(name="dash")
def dash(value):
    return value.replace(" ", "-")
