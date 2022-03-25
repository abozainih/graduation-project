import phonenumbers
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    order_customer_name = serializers.SerializerMethodField()
    order_customer_phonenumber = serializers.SerializerMethodField()
    order_total_price = serializers.SerializerMethodField()
    order_status = serializers.SerializerMethodField()

    def get_order_customer_name(self,obj):
        return obj.made_for.get_full_name()

    def get_order_customer_phonenumber(self, obj):
        return str(phonenumbers.format_number(obj.made_for.phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))

    def get_order_total_price(self, obj):
        return obj.made_for.user_customer.all()[0].price_per_gallon * obj.num_of_gallon

    def get_order_status(self, obj):
        return obj.get_order_status_display()

    class Meta:
        model = Order
        fields = ['order_date', 'order_status', 'is_paid', 'order_customer_name', 'order_customer_phonenumber', 'num_of_gallon', 'order_total_price']
