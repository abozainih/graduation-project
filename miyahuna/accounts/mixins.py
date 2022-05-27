from django.contrib.auth.mixins import AccessMixin


class AdminAndEmployeeMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_staff or (hasattr(request.user, 'Employee_user') and not request.user.is_active):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AdminMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class CustomerMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not hasattr(request.user, 'user_customer'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
