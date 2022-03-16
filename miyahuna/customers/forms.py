from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from customers.models import Customer


class CreateCustomerForm(UserCreationForm):

    price_per_gallon = forms.DecimalField(max_digits=5, decimal_places=2, label=_("Price per gallon"))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Customer.objects.create(user=user, price_per_gallon=self.cleaned_data["price_per_gallon"])
        return user


class UpdateCustomerForm(forms.ModelForm):

    price_per_gallon = forms.DecimalField(max_digits=5, decimal_places=2, label=_("Price per gallon"))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2', 'price_per_gallon']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'