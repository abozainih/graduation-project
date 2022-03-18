from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from accounts.models import User
from employees.forms import CreateDataEntryEmployeeForm, CreateEmployeeForm


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