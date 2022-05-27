from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import User


class loginForm(AuthenticationForm):

    username = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'rtl'
        self.helper.add_input(Submit('submit', _('login'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))



class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('save'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))




class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('save'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))

