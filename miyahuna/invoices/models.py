from django.db import models

# Create your models here.
from orders.models import Order


class Debit(models.Model):

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.BooleanField()

    class Meta:
        app_label = "invoices"

    def __str__(self):
        self.order.made_for.user.get_full_name()
