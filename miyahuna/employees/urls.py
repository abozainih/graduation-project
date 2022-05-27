from django.urls import path, include
from . import views
from .api import urls
urlpatterns = [
    path('list/', views.EmployeesListView.as_view(), name='EmployeesList'),
    path('create/DataEntry/', views.DataEntryEmployeeCreateView.as_view(), name='CreateDataEntryEmployee'),
    path('create/', views.EmployeeCreateView.as_view(), name='CreateEmployee'),
    path('create/Absence/<pk>', views.AbsenceCreateView.as_view(), name='CreateAbsence'),
    path('update/<pk>/', views.EmployeeUpdateView.as_view(), name='UpdateEmployee'),
    path('Absence/<pk>/', views.AbsenceListView.as_view(), name='AbsenceList'),
    path('api/', include(urls)),
#
]
