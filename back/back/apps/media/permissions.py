from rest_framework import permissions


class OwnMediaPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own media
    """

    def has_object_permission(self, request, view, obj):
        # Only auth requests,
        if not request.user.is_authenticated:
            return False

        if not obj:  # or request.user.is_staff:
            return True

        # obj here is a Media instance
        return obj.user == request.user
