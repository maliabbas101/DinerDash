from django.db import models

from django.contrib.postgres.fields import ArrayField

from customers.models.customer import Customer


class Session(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = ArrayField(
        ArrayField(
            models.CharField(max_length=255),

        ),
    )
    def save_session(self):
        self.save()
    def get_session_by_id(customer):
        return Session.objects.filter(customer=customer)


