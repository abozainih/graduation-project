from django import forms
from phonenumber_field.formfields import PhoneNumberField
from accounts.models import User
from orders.models import Order
from django.utils.translation import gettext_lazy as _



class CreateOrderForm(forms.ModelForm):

    customer_name = forms.CharField(required=False, label=_('customer name'))
    phone_number = PhoneNumberField(required=True, label=_('phone number'))

    class Meta:
        fields = ['customer_name', 'phone_number', 'num_of_gallon']
        model = Order


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
