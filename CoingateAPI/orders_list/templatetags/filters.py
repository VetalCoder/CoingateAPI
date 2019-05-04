from django import template

register = template.Library()

@register.filter(name="to_list")
def list_from_number(value):
    return [index for index in range(1, value + 1)]
