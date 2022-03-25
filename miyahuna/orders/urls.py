from django.urls import path, include
from . import views
from .api import urls
urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='CreateOrder'),
    path('list/', views.OrderListView.as_view(), name='OrderList'),
    path('api/', include(urls)),
]
