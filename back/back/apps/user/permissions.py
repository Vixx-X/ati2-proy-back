from django.utils.translation import gettext_lazy as _
from rest_framework import permissions


class IsSameUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Only create object new objects,
        # so we'll always allow HEAD or OPTIONS requests.
        if request.method in ["HEAD", "OPTIONS"]:
            return True

        # Instance must have an attribute named `owner`.
        return obj == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Only create object new objects,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # view must have the instance attribute named `user_attr` else `user`.
        return getattr(obj, getattr(view, "user_attr", "user")) == request.user
