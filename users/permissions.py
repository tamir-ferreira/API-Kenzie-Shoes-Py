from rest_framework import permissions
from .models import User
from rest_framework.views import *


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and request.user == obj or request.user.is_staff


class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_staff:
            return True
