from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """ полные права на управление всем контентом проекта.
    Может создавать и удалять произведения,
    категории и жанры. Может назначать роли пользователям. """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)