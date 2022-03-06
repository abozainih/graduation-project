from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import loginForm


class loginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = loginForm
    authentication_form = None
    next_page = reverse_lazy("mainpanel")
    redirect_field_name =  None
    redirect_authenticated_user = True




class MainPanelView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/admin_panel.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'