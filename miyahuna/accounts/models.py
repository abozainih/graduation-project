
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    phone_number = PhoneNumberField(unique=True,region="PS")


    def __str__(self):
        return self.username
