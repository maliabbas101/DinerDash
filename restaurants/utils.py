from restaurants.models.order import Order
from restaurants.models.order_items import OrderItem


def cart_quantity(item, cart, remove):
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
    orderobject = order_op[0]
    return orderobject


def creating_pending_orders(cart, customer, remove, item_ord, item):

    pending_orders = Order.get_orders_by_customer_and_status(
        customer)

    if pending_orders.count() == 0 and not remove:
        pending_order = Order(customer=customer, price="0")

        pending_order.save()
    else:
        pending_order = pending_orders[0]

    if not remove:
        checkifOrder = OrderItem.if_order_item(
            item_ord, order=pending_order)
        if checkifOrder:
            order_item = OrderItem.objects.filter(
                item=item_ord, order=pending_order)[0]
            order_item.item_quantity += 1
            order_item.save()
        else:

            order_item = OrderItem(
                item=item_ord, order=pending_order, item_price=item_ord.price, item_quantity=cart.get(item))
            order_item.save()

        pending_order.price = str(
            int(pending_order.price)+item_ord.price)
        pending_order.restaurant = item_ord.restaurant
        pending_order.save()
    else:

        pending_order.price = str(
            int(pending_order.price) - item_ord.price)
        pending_order.save()
        order_item = OrderItem.objects.filter(
            item=item_ord, order=pending_order)[0]

        if order_item.item_quantity == 1:
            OrderItem.objects.filter(item=item_ord).delete()
        else:
            order_item.item_quantity -= 1
            order_item.save()
