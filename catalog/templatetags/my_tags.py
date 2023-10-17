from django import template

register = template.Library()


@register.filter()
def mediapath(value):
    if value:
        return f'/media/{value}'

    return f'/static/images/no_image.jpg'