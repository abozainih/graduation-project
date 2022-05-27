from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Order(models.Model):

    pending = 0
    done = 1
    rejected = 2

    status = [(pending, _('pending')),
              (done, _('done')),
              (rejected, _('rejected'))
              ]

    num_of_gallon = models.IntegerField(blank=False, verbose_name=_("number of gallons"))
    made_by = models.ForeignKey(User, related_name="user_orders",on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True, verbose_name=_("order date"))
    order_status = models.IntegerField(default=pending, choices=status, verbose_name=_('order status'))
    made_for = models.ForeignKey(User, related_name="m_user_orders", on_delete=models.CASCADE)

    def __str__(self):
        return self.made_for.get_full_name() + " Order"
