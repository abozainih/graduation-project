from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.OrdersPendingListView.as_view(), name="OrdersPendingListView"),
    path('history/', views.OrdersHistoryListView.as_view(), name="OrdersHistoryListView"),
    path('<pk>', views.CustomerOrdersListView.as_view(), name="CustomerOrdersListView"),
]
