from django import template

register = template.Library()


@register.filter('is_admin')
def is_admin(str):
    if str == 'admin':
        return True
    return False
