from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.method in permissions.SAFE_METHODS or
                    request.user.is_authenticated)

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.author == request.user
