from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    message = 'Изменять или удалять объект может только его владелец.'

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        author = getattr(obj, 'author', None)

        if author is None:
            return False

        owner_user = getattr(author, 'user', None)
        if owner_user is None:
            return False

        return owner_user.id == getattr(request.user, 'id', None)

        # if request.user.is_staff or request.user.is_superuser:
        #     return True