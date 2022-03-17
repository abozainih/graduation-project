import django.views.generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# Create your views here.
import accounts.models
from customers.forms import UpdateCustomerForm, CreateCustomerForm
from customers.models import Customer


class CustomersListView(LoginRequiredMixin, TemplateView):
    template_name = "customers/customersList.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'


class CustomersCreateView(LoginRequiredMixin, django.views.generic.CreateView):
    template_name = "customers/addCustomer.html"
    login_url = reverse_lazy("login")
    model = accounts.models.User
    form_class = CreateCustomerForm
    success_url = reverse_lazy("CustomersList")


class CustomersUpdateView(LoginRequiredMixin, django.views.generic.UpdateView):
    template_name = "customers/updateCustomer.html"
    login_url = reverse_lazy("login")
    model = accounts.models.User
    success_url = reverse_lazy("CustomersList")
    form_class= UpdateCustomerForm


    def get_object(self, queryset=None):
        customer = Customer.objects.get(pk=self.kwargs['pk'] )
        return accounts.models.User.objects.get(pk=customer.user.id)


    def get_initial(self):
        initial = super().get_initial()
        customer = Customer.objects.get(user=self.get_object())
        initial['price_per_gallon'] = customer.price_per_gallon
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        customer = Customer.objects.get(user = form.instance)
        customer.price_per_gallon = form.cleaned_data['price_per_gallon']
        form.instance.save()
        customer.save()
        return response
