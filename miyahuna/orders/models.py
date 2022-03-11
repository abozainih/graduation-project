from django.db import models
from accounts.models import User
# Create your models here.


class Order(models.Model):

    num_of_gallon = models.IntegerField(blank=False)
    madeBy = models.ForeignKey(User,related_name="user_orders",on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField()
    status = models.BooleanField(default=False)


    def __str__(self):

        return self.madeBy.get_full_name() + " Order"
