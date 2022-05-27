
def rules_processor(request):
     return {
         'isAdmin': request.user.is_staff,
         'isEmployee': request.user.is_active and hasattr(request.user, 'employee_user'),
         'isCustomer': request.user.is_active and hasattr(request.user, 'user_customer'),
    }