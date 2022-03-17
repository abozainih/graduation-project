from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView

from accounts.models import User
from customers.models import Customer
from orders.models import Order
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views


from accounts.forms import loginForm, UpdateProfileForm, ChangePasswordForm


class loginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = loginForm
    authentication_form = None
    next_page = reverse_lazy("mainpanel")
    redirect_field_name =  None
    redirect_authenticated_user = True


class logOutView(LogoutView):
    next_page = reverse_lazy("login")
    template_name = None
    redirect_field_name = None




class MainPanelView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/admin_panel.html"
    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = {
            'CustomersCount': Customer.objects.count(),
            'OrdersCount': Order.objects.filter(status='False').count(),
        }
        context.update(extra_context)

        return context


class UpdateProfileView(UpdateView):
    model = User
    template_name = 'accounts/updateProfile.html'
    success_url = reverse_lazy("mainpanel")
    form_class = UpdateProfileForm

    def get_object(self, query_set=None):
        return self.request.user


class ChangePasswordView(auth_views.PasswordChangeView):

    template_name = 'accounts/changePassword.html'
    success_url = reverse_lazy('mainprofile')
    form_class = ChangePasswordForm
