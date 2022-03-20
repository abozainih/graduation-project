from rest_framework.permissions import IsAdminUser

from .serializers import EmployeeSerializer, AbsenceSerializer
from employees.models import Employee, Absence
from rest_framework import generics, serializers


class EmployeesListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]


class AbsenceListView(generics.ListAPIView):
    serializer_class = AbsenceSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Absence.objects.filter(employee_id=self.kwargs['pk']).order_by('-ab_date')
