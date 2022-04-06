from django.urls import include, path
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'list', views.CustomerListView)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     ]

urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name="CustomersListApi"),
    path('create/', views.CustomerCreateView.as_view(), name="createCust"),
    path('update/<pk>', views.CustomerUpdateView.as_view(), name='updateCust'),
    path('search/', views.CustomerFilterView.as_view(), name='Search')
]