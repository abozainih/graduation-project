import datetime
from decimal import Decimal

import django.views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View

from accounts.models import User
from customers.models import Customer
from .forms import CreateOrderForm
from .models import Order
# Create your views here.
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect


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


class AcceptOrder(LoginRequiredMixin, django.views.View):
    http_method_names = ['post']
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.order_status = 1
        order.save()
        return redirect("OrderList")

class RejectOrder(LoginRequiredMixin, django.views.View):
    http_method_names = ['post']
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.order_status = 2
        order.save()
        return redirect("OrderList")


class OrderHistory(LoginRequiredMixin, TemplateView):
    template_name = "orders/orderHistory.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'


class CustomerOrderHistory(LoginRequiredMixin, TemplateView):
    template_name = "orders/customerOrderHistory.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"customer": Customer.objects.get(pk=self.kwargs['pk'])})
        return context


class OrdersSalesCount(LoginRequiredMixin, View):

    def get(self, request, start, end):
        orders = Order.objects.filter(order_status=1, order_date__range=[start, end])
        sum = 0
        for obj in orders:
            sum += obj.made_for.user_customer.all()[0].price_per_gallon * obj.num_of_gallon

        sum = Decimal(sum).normalize()
        return JsonResponse({'ordersSales': sum})
