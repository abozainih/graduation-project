from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)


class BasicData(models.Model):

    phone_number_exists = {
        'unique': _("theres already a user that have this phone number!"),
    }
    first_name = models.CharField(verbose_name=_('First name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=50)
    phone_number = PhoneNumberField(unique=True, region="PS", blank=False, null=False, verbose_name=_('Phone Number'), error_messages=phone_number_exists)
    address_1 = models.CharField(max_length=400,verbose_name=_('Address 1'),blank=True)
    address_2 = models.CharField(max_length=400, verbose_name=_('Address 2'), blank=True)
    USERNAME_FIELD = 'phone_number'

    def get_full_name(self):

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        abstract = True


class User(BasicData, AbstractBaseUser, PermissionsMixin):

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('Is valid account'), default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

