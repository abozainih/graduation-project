from django.urls import reverse
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
import accounts.api.serializers
from customers.models import Customer
from orders.models import Order
from accounts.models import User
import phonenumbers


class CustomerSerializer(serializers.ModelSerializer):

    customer_name= serializers.SerializerMethodField()
    customer_PhoneNumber = serializers.SerializerMethodField()
    customer_lastOrderDate = serializers.SerializerMethodField()
    # customer_allsales = serializers.SerializerMethodField()
    customer_update_link = serializers.SerializerMethodField()

    def get_customer_name(self,obj):
        return obj.user.get_full_name()

    def get_customer_PhoneNumber(self, obj):
        return str(phonenumbers.format_number(obj.user.phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))

    def get_customer_lastOrderDate(self,obj):

        if Order.objects.filter(madeBy=obj.user).exists():
            return Order.objects.filter(madeBy=obj.user).latest('order_date').order_date
        else:
            return _("there's no orders")

    def get_customer_update_link(self, obj):
         return reverse('UpdateCustomer', kwargs={'pk': obj.pk})


    class Meta:
        model = Customer
        fields = ['price_per_gallon', 'customer_name', 'customer_PhoneNumber', 'customer_lastOrderDate', 'customer_update_link']


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

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        instance.price_per_gallon = validated_data.get('price_per_gallon', instance.price_per_gallon)
        instance.save()
        user.username = user_data.get('username',user.username)
        user.last_name = user_data.get('last_name', user.last_name)
        user.first_name = user_data.get('first_name', user.first_name)
        user.email = user_data.get('email', user.email)
        user.password = user_data.get('password', user.password)
        user.phone_number = user_data.get('phone_number', user.phone_number)
        user.save()

        return instance
