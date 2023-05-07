from rest_framework import serializers
from .models import *


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "user_id"]
        read_only_fields = ["id", "user_id"]


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = ["id", "quantities", "cart_id", "product_id"]

        depth = 1

        read_only_fields = ["id", "cart_id", "product_id"]

