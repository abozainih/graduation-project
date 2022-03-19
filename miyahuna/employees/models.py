from django.db import models
from accounts.models import BasicData, User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Employee(models.Model):

    salary_per_day = models.DecimalField(max_digits=5, decimal_places=2, blank=False, verbose_name=_("salary per day"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_user", blank=True, null=True)

    class Meta:
        app_label = 'employees'

    def __str__(self):
        return self.user.get_full_name()


class Absence(models.Model):

    ab_date = models.DateField(auto_now_add=True, verbose_name=_('absence date'))
    is_paid = models.BooleanField(default=False, verbose_name=_('is paid ?'))
    employee = models.ForeignKey(Employee, related_name='employee_absence', on_delete=models.CASCADE)

    class Meta:
        app_label = 'employees'


    def __str__(self):
        return self.employee.user.get_full_name()
