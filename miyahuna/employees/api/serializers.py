import phonenumbers
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    employee_name= serializers.SerializerMethodField()
    employee_PhoneNumber = serializers.SerializerMethodField()
    is_data_entry = serializers.SerializerMethodField()
    # employee_allsales = serializers.SerializerMethodField()

    def get_employee_name(self, obj):
        return obj.user.get_full_name()

    def get_employee_PhoneNumber(self, obj):

        return str(phonenumbers.format_number(obj.user.phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))

    def get_is_data_entry(self, obj):
        return str(obj.user.is_active)


    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_PhoneNumber', 'is_data_entry', 'salary_per_day']