from django import template

register = template.Library()


@register.filter(name='in_cart')
def in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart_quan')
def cart_quan(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='total_price')
def total_price(product, cart):
    return product.price * cart_quan(product, cart)

@register.filter(name='grand_total')
def grand_total(product, cart):
    sum = 0
    for p in product:
        sum += total_price(p, cart)
    return sum

@register.filter(name='calc')
def grand_total(n1, n2):
    return n1*n2
