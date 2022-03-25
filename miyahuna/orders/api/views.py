from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from orders.api.serializers import OrderSerializer
from orders.models import Order


class OrdersPendingListView(generics.ListAPIView):
    queryset = Order.objects.filter(order_status=0)
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]