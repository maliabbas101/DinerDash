from django.db import models
# from restaurants.models import order,item


class OrderItem(models.Model):
    item = models.ForeignKey(
        'restaurants.Item', related_name='order_item', on_delete=models.CASCADE)
    order = models.ForeignKey('restaurants.Order', related_name='order_item',
                              on_delete=models.CASCADE, null=True, blank=True)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField(default=0)

    @staticmethod
    def get_orders_by_ids(orders):
        return OrderItem.objects.filter(order__in=orders)

    @staticmethod
    def if_order_item(item, order):
        order_items = OrderItem.objects.filter(item=item, order=order)
        if order_items.count() > 0:
            return True
        return False
