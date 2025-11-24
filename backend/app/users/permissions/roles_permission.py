#users/permissions/roles_permission.py

from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Allows access only to users with admin role."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
    
class IsStaff(permissions.BasePermission):
    """Allows access only to users with 'staff' role."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'staff'
    
class IsCustomer(permissions.BasePermission):
    """Allows access only to users with 'customer' role."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'customer'
    
class IsAdminOrStaff(permissions.BasePermission):
    """Allows access to users with 'admin' or 'staff' roles."""

    def has_permission(self, request, view, obj):

        # Admin can be anything
        if request.user.role == 'admin' or request.user.is_superuser:
            return True
        return request.user and request.user.is_authenticated and request.user.role in ['admin', 'staff']
    

    
