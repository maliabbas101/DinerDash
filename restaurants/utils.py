from restaurants.models.orders import Order
def cart_quantity(item,cart,remove):
      if cart:
        quantity = cart.get(item)
        if quantity:
            if remove:
                if quantity == 1:
                    cart.pop(item)
                else:
                    cart[item] = quantity-1
            else:
                cart[item] = quantity+1
        else:
            cart[item] = 1
      else:
          cart = {}
          cart[item] = 1

      return cart

def get_order(order_id):
    order_op = Order.get_order_by_id(order_id)
    orderobject = order_op [0]
    return orderobject

