from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from accounts.models import User
from employees.forms import CreateDataEntryEmployeeForm, CreateEmployeeForm, UpdateEmployeeForm
from employees.models import Employee


class EmployeesListView(LoginRequiredMixin, TemplateView):
    template_name = "employees/employeesList.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'


class DataEntryEmployeeCreateView(LoginRequiredMixin, CreateView):
    template_name = "employees/addDataEntryEmployee.html"
    login_url = reverse_lazy("login")
    model = User
    form_class = CreateDataEntryEmployeeForm
    success_url = reverse_lazy("EmployeesList")


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    template_name = "employees/addEmployee.html"
    login_url = reverse_lazy("login")
    model = User
    form_class = CreateEmployeeForm
    success_url = reverse_lazy("EmployeesList")



class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "employees/updateEmployee.html"
    login_url = reverse_lazy("login")
    model = User
    success_url = reverse_lazy("EmployeesList")
    form_class = UpdateEmployeeForm


    def get_object(self, queryset=None):
        employee = Employee.objects.get(pk=self.kwargs['pk'] )
        return User.objects.get(pk=employee.user.id)


    def get_initial(self):
        initial = super().get_initial()
        employee = Employee.objects.get(user=self.get_object())
        initial['salary_per_day'] = employee.salary_per_day
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        employee = Employee.objects.get(user=form.instance)
        employee.salary_per_day = form.cleaned_data['salary_per_day']
        form.instance.save()
        employee.save()
        return response