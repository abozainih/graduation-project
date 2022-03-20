import phonenumbers
from django.urls import reverse
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from employees.models import Employee, Absence
import datetime

class EmployeeSerializer(serializers.ModelSerializer):

    employee_name= serializers.SerializerMethodField()
    employee_PhoneNumber = serializers.SerializerMethodField()
    is_data_entry = serializers.SerializerMethodField()
    employee_update_link = serializers.SerializerMethodField()
    absences_count = serializers.SerializerMethodField()
    add_absence_url = serializers.SerializerMethodField()

    def get_employee_name(self, obj):
        return obj.user.get_full_name()

    def get_employee_PhoneNumber(self, obj):

        return str(phonenumbers.format_number(obj.user.phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))

    def get_is_data_entry(self, obj):
        return str(obj.user.is_active)

    def get_employee_update_link(self, obj):
         return reverse('UpdateEmployee', kwargs={'pk': obj.pk})

    def get_absences_count(self, obj):
        today = datetime.date.today()
        return Absence.objects.filter(employee=obj, ab_date__month=today.month).count()

    def get_add_absence_url(self, obj):
        return reverse('CreateAbsence', kwargs={'pk': obj.pk})


    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_PhoneNumber', 'is_data_entry', 'salary_per_day', 'employee_update_link', 'absences_count', 'add_absence_url']
