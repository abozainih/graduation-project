from accounts.models import User
from .serializers import CustomerSerializer, CustomerUser
from customers.models import Customer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerUser
    permission_classes = [IsAdminUser]

