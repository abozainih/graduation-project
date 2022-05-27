from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import redirect, get_object_or_404
from rest_framework.response import Response

from accounts.models import User
from .serializers import CustomerSerializer, CustomerUser
from customers.models import Customer
from rest_framework import generics, serializers
from . import access


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [access.IsAdminUser]


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerUser
    permission_classes = [access.IsAdminUser]

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('CustomersList')


class CustomerFilterView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        query = Customer.objects.annotate(fullname=Concat('user__first_name', Value(' '), 'user__last_name'))
        return query.filter(fullname__icontains=self.request.GET['data'])



class CustomerUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerUser
    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(Customer, pk=pk)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        customer = Customer.objects.get(pk=pk)
        user = User.objects.get(pk=customer.user.id)
        data = request.data
        errors = serializers.ValidationError()
        if customer.user.username != data['user']['username']:
            if not User.objects.filter(username=data['user']['username']).exists():
                customer.user.username = data['user']['username']
            else:
                errors.detail ={'username': 'Please enter a valid name.'}
        else:
            customer.user.username = data['user']['username']

        if customer.user.phone_number != data['user']['phone_number']:
            if not User.objects.filter(phone_number=data['user']['phone_number']).exists():
                customer.user.phone_number = data['user']['phone_number']
            else:
                errors.detail.update({'phone_numer': 'Please enter a valid number.'})
        else:
            customer.user.phone_number = data['user']['phone_number']

        if customer.user.email != data['user']['email']:
            if not User.objects.filter(email=data['user']['email']).exists():
                customer.user.email = data['user']['email']
            else:
                errors.detail.update({'email':'Please enter a valid email.'})
        else :
            customer.user.email = data['user']['email']

        if errors.detail:
            raise errors

        customer.price_per_gallon = data['price_per_gallon']
        customer.user.first_name = data['user']['first_name']
        customer.user.last_name = data['user']['last_name']
        customer.save()
        user.first_name = customer.user.first_name
        user.last_name = customer.user.last_name
        user.email=customer.user.email
        user.phone_number=customer.user.phone_number
        user.username=customer.user.username
        user.save()
        s = CustomerUser(customer)
        return Response(s.data)
