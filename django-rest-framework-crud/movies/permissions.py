from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from authentication.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE' and\
        (request.user.role == User.role.superuser or  request.user.role == User.role.admin):
            return True
        
        elif request.method == 'GET':
            return True