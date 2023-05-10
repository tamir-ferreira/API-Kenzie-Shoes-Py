from rest_framework import permissions
from .models import Cart
from rest_framework.views import *


class IsBuyAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Cart) -> bool:
        user = Cart.objects.filter(user_id=request.user.id)
        cart_obj = user.filter(id=obj.id)
        return request.user.is_authenticated and user and cart_obj
