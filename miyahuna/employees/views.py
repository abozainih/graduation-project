from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class EmployeesListView(LoginRequiredMixin, TemplateView):
    template_name = "employees/employeesList.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'