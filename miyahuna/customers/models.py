from django.db import models
from accounts.models import User
# Create your models here.

class Customer(models.Model):

    price_per_gallon =  models.DecimalField(max_digits=5,decimal_places=2)
    user = models.ForeignKey(User,related_name="user_customer",on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.user.get_full_name()
