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
    path('list/', views.EmployeesListView.as_view(), name="employeelistapi"),
    path('list/Absence/<pk>', views.AbsenceListView.as_view(), name="absencelistapi"),
]