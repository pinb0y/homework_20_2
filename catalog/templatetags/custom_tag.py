from django import template


register = template.Library()

@register.filter
def make_image_link(data):
    if data:
        return f'/media/{data}'
    return '#'