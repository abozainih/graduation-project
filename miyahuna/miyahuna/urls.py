
from django.contrib import admin
from django.urls import path,include
from accounts import views


urlpatterns = [
    path('', views.MainPanelView.as_view(), name='mainpanel'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('customers/', include("customers.urls")),
    path('employees/', include("employees.urls")),
    path('orders/', include("orders.urls")),

]
