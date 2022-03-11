
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):

    phone_number = PhoneNumberField(unique=True, region="PS", blank=False, null=False)
    address_1 = models.TextField()
    address_2 = models.TextField()

    def __str__(self):
        return self.username
