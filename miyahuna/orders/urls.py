from django.urls import path, include
from . import views
from .api import urls
urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='CreateOrder'),
    path('Customer/create/', views.CustomerOrderCreateView.as_view(), name='CustomerCreateOrder'),
    path('list/', views.OrderListView.as_view(), name='OrderList'),
    path('accept/<pk>', views.AcceptOrder.as_view(), name='AcceptOrder'),
    path('reject/<pk>', views.RejectOrder.as_view(), name='RejectOrder'),
    path('history/', views.OrderHistory.as_view(), name='OrderHistory'),
    path('last-year/', views.LastYearSales.as_view(), name='LastYearSales'),
    path('<int:pk>', views.CustomerOrderHistory.as_view(), name='CustomerOrderHistory'),
    path('sales/<start>/<end>', views.OrdersSalesCount.as_view(), name="OrdersSales"),
    path('api/', include(urls)),
]
