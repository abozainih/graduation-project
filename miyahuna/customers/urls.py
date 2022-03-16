from django.urls import path, include
from . import views
from .api import urls

urlpatterns = [
    path('list/', views.CustomersListView.as_view(), name='CustomersList'),
    path('create/', views.CustomersCreateView.as_view(), name='CreateCustomer'),
    path('update/<pk>/', views.CustomersUpdateView.as_view(), name='UpdateCustomer'),
    path('api/', include(urls)),

]