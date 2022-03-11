from rest_framework import serializers

import accounts.api.serializers
from customers.models import Customer
from orders.models import Order
from accounts.models import User


class CustomerSerializer(serializers.ModelSerializer):

    customer_name= serializers.SerializerMethodField()
    customer_PhoneNumber = serializers.SerializerMethodField()
    customer_lastOrderDate = serializers.SerializerMethodField()
    # customer_allsales = serializers.SerializerMethodField()

    def get_customer_name(self,obj):
        return obj.user.get_full_name()

    def get_customer_PhoneNumber(self,obj):
        return str(obj.user.phone_number)

    def get_customer_lastOrderDate(self,obj):

        if Order.objects.filter(madeBy=obj.user).exists():
            return Order.objects.filter(madeBy=obj.user).latest('order_date').order_date
        else:
            return "لا يوجد طلبات..."

    class Meta:
        model = Customer
        fields = ['price_per_gallon', 'customer_name', 'customer_PhoneNumber', 'customer_lastOrderDate']


class CustomerUser(serializers.ModelSerializer):

    user = accounts.api.serializers.UserSerializer()

    class Meta:
        model = Customer
        fields = ['user', 'price_per_gallon']

    def create(self, validated_data):
        user = validated_data.pop('user')
        u = User.objects.create(**user)
        customer = Customer.objects.create(user=u, **validated_data)
        return customer
