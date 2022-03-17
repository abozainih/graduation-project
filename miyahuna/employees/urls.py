from django.urls import path, include
from . import views
from .api import urls
urlpatterns = [
    path('list/', views.EmployeesListView.as_view(), name='EmployeesList'),
#     path('create/', views.EmployeeCreateView.as_view(), name='CreateEmployee'),
#     path('update/<pk>/', views.EmployeeUpdateView.as_view(), name='UpdateEmployee'),
     path('api/', include(urls)),
#
]
