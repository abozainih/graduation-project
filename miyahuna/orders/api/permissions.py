from django.http import Http404

from rest_framework import exceptions
from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class isEmployee(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active and hasattr(request.user, 'employee_user'))

class isCustomer(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active and hasattr(request.user, 'user_customer'))
