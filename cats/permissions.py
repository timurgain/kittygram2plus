from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """этот пермишн сработает как надо только если у объекта есть поле owner."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS