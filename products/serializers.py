from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer
from cart.serializers import CartSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        user = UserSerializer()
        cart = CartSerializer
        # fields = "__all__"
        fields: [
            "id",
            "name",
            "value",
            "category",
            "quantities",
            "bio",
            "image_product",
            "user",
            "cart",
        ]
        read_only_fields = ["id", "user", "cart"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
