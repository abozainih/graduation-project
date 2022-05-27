from django import forms
from phonenumber_field.formfields import PhoneNumberField
from accounts.models import User
from orders.models import Order
from django.utils.translation import gettext_lazy as _



class CreateOrderForm(forms.ModelForm):

    customer_name = forms.CharField(required=True, label=_('customer name'))
    phone_number = PhoneNumberField(required=True, label=_('phone number'))

    class Meta:
        fields = ['customer_name', 'phone_number', 'num_of_gallon']
        model = Order


class CustomerCreateOrderForm(forms.ModelForm):

    class Meta:
        fields = ['num_of_gallon']
        model = Order
