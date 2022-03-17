from rest_framework.permissions import IsAdminUser

from .serializers import EmployeeSerializer
from employees.models import Employee
from rest_framework import generics, serializers


class EmployeesListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]