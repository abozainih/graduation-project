from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext_lazy as _
from employees.models import Employee


class CreateDataEntryEmployeeForm(UserCreationForm):

    salary_per_day = forms.DecimalField(max_digits=5, decimal_places=2, label=_("salary per day"))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('save'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Employee.objects.create(user=user, salary_per_day=self.cleaned_data["salary_per_day"])
        return user



class CreateEmployeeForm(UserCreationForm):

    salary_per_day = forms.DecimalField(max_digits=5, decimal_places=2, label=_("salary per day"))
    password1 = forms.CharField(widget=forms.HiddenInput())
    password2 = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('save'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        if commit:
            user.save()
            Employee.objects.create(user=user, salary_per_day=self.cleaned_data["salary_per_day"])
        return user


class UpdateEmployeeForm(forms.ModelForm):

    salary_per_day = forms.DecimalField(max_digits=5, decimal_places=2, label=_("salary per day"))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'address_1', 'address_2', 'salary_per_day']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('save'), css_class='btn btn-gradient-primary font-weight-medium auth-form-btn'))

