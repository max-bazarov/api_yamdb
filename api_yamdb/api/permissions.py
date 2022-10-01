from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    obj.author == request.user
                    or request.user.is_moderator
                )
            )
        )


class OwnerOrAdmins(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_admin
                or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj == request.user
            or request.user.is_admin
            or request.user.is_superuser)


class OwnerOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj == request.user
            or request.user.is_staff)


class AuthorStaffOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (
            obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        ):
            return True


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_staff
            or request.user.is_admin
        )
