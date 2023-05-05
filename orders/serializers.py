from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import *
from products.serializers import ProductSerializer
from users.serializers import UserSerializer
from .models import UserOrder


class OrderSerializer(serializers.ModelSerializer):

    user_buy = serializers.EmailField(source="user.email", read_only=True)
    products = ProductSerializer

    # def create(self, validated_data: dict) -> UserOrder:

    class Meta:
        model = UserOrder
        fields = [
            "id",
            "status",
            "buyed_at",
            "user_buy",
            "products",
        ]

        depth = 1

        read_only_fields = ["id", "buyed_at", "products"]