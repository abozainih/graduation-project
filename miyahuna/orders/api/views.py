from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from customers.models import Customer
from orders.api.serializers import OrderSerializer
from orders.models import Order


class OrdersPendingListView(generics.ListAPIView):
    queryset = Order.objects.filter(order_status=0)
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

class OrdersHistoryListView(generics.ListAPIView):
    queryset = Order.objects.order_by('-order_date')
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class CustomerOrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        customer = Customer.objects.get(pk=self.kwargs['pk'])
        return customer.user.m_user_orders.order_by('-order_date')
