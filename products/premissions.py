from rest_framework import permissions
from rest_framework.views import *


class IsAdminAndSellerCreateUpdatedDestroy(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (request.method in permissions.SAFE_METHODS or request.user and request.user.is_seller or request.user.is_staff)


