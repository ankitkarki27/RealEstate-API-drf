from rest_framework import permissions, status

class IsRealtorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow Realtors to edit listings.
    """

    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write access only to Realtors
        return request.user.is_authenticated and request.user.role == "realtor"