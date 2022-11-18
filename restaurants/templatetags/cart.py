from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(item, cart):
    if str(item.id) in cart:
        return True
    return False


@register.filter(name='cart_count')
def cart_count(item, cart):
    if str(item.id) in cart:
        return cart[str(item.id)]
    return 0


@register.filter(name='currency')
def currency(number):
    return str(number)+'$'


@register.filter(name='is_cart_empty')
def is_cart_empty(cart):
    if len(cart.keys()) == 0:
        return True
    return False


@register.filter(name='item_total')
def item_total(item, cart):
    return item.price * cart_count(item, cart)


@register.filter(name='total_amount')
def total_amount(items, cart):
    sum = 0
    for item in items:
        sum += item_total(item, cart)
    return sum


@register.filter('is_admin')
def is_admin(string):
    if str(string) == 'admin':
        return True
    return False

@register.filter('is_user')
def is_user(string):
    if str(string) == 'user':
        return True
    return False

@register.filter('is_retired')
def is_retired(item):
    if item.retired == True:
        return True
    return False

@register.filter('is_owner')
def is_owner(restaurant,fullname):
    if restaurant.owner.full_name == fullname:
        return True
    return False
