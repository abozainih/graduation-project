from rest_framework import generics

from .permissions import IsAdminUser, isEmployee, isCustomer

from customers.models import Customer
from orders.api.serializers import OrderSerializer
from orders.models import Order


class OrdersPendingListView(generics.ListAPIView):
    queryset = Order.objects.filter(order_status=0)
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | isEmployee]

class OrdersHistoryListView(generics.ListAPIView):
    queryset = Order.objects.order_by('-order_date')
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | isEmployee]


class CustomerOrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | isEmployee]

    def get_queryset(self):
        customer = Customer.objects.get(pk=self.kwargs['pk'])
        return customer.user.m_user_orders.order_by('-order_date')



class CustomerOrdersHistoryListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [isCustomer]

    def get_queryset(self):
        customer = Customer.objects.get(pk=self.request.user.user_customer.all()[0].pk)
        return customer.user.m_user_orders.order_by('order_status')


