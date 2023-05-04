from django.shortcuts import render
from cart.serializers import CartSerializer
from .models import Cart
from rest_framework.generics import *
from users.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = self.request.cart
        queryset = super().get_queryset()
        return queryset.filter(cart=cart)
