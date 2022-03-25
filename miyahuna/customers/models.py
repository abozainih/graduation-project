from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Customer(models.Model):

    price_per_gallon = models.DecimalField(max_digits=5,decimal_places=2, verbose_name=_("Price Per Gallon"))
    user = models.ForeignKey(User, related_name="user_customer", on_delete=models.CASCADE, blank=False, verbose_name=_("User"))

    def __str__(self):
        return self.user.get_full_name()
