# Permissions, разрешения
# Разрешения позволяют разграничить права доступа к операциям.
# Собственные классы разрешений
from rest_framework import permissions


# Кастомные классы разрешений наследуются от базового класса BasePermission.
# В нем определены два метода:
# has_permission (разрешение на уровне запроса),
# has_object_permission (разрешение на уровне объекта).
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or
                    request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff
