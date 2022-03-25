from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from accounts.models import User
from .forms import CreateOrderForm
from .models import Order
# Create your views here.
from django.views.generic import CreateView, TemplateView


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = "orders/CreateOrder.html"
    login_url = reverse_lazy("login")
    form_class = CreateOrderForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy("OrderList")


    def form_valid(self, form):
        form.instance.made_for = User.objects.get(phone_number=form.cleaned_data['phone_number'])
        form.instance.made_by = self.request.user
        form.instance.order_status = 0
        response = super().form_valid(form)
        form.instance.save()
        return response


class OrderListView(LoginRequiredMixin, TemplateView):
    template_name = "orders/ordersList.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'
