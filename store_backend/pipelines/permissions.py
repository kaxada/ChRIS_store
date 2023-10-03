
from rest_framework import permissions


class IsChrisOrOwnerOrNotLockedReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or superuser
    'chris' to modify/edit it. Read only is allowed to other users only
    when object is not locked.
    """

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS) and not obj.locked:
            # Read permissions are allowed to any user if object is not locked
            return True

        # superuser 'chris' and owner always have read/write access
        return (request.user == obj.owner) or (request.user.username == 'chris')


class IsChrisOrOwnerAndLockedOrNotLockedReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow read/write access to the Superuser Chris or the
    object's owner when corresponding pipeline is locked. Read only access is granted to
    any user when corresponding pipeline is not locked.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.username == 'chris':
            # superuser 'chris' always has read/write access
            return True

        pipeline = obj.plugin_piping.pipeline
        return (
            request.user == pipeline.owner
            if pipeline.locked
            else request.method in permissions.SAFE_METHODS
        )


class IsChrisOrOwnerOrNotLocked(permissions.BasePermission):
    """
    Custom permission to only allow access to the Superuser Chris or the object's owner.
    Access is granted to any other user when corresponding pipeline is not locked.
    """

    def has_object_permission(self, request, view, obj):
        pipeline = obj.pipeline
        if not pipeline.locked:
            return True
        # superuser 'chris' and owner always have read/write access
        return (request.user == pipeline.owner) or (request.user.username == 'chris')
