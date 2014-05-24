from rest_framework import permissions
from timebook.models import Worker


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission that only allows access for user and
    admins.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.worker == Worker.objects.get(user=request.user)
