from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer
from users.models import User
from cart.serializers import CartSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        user = UserSerializer
        cart = CartSerializer
        fields = "__all__"
        # fields: [
        #     "id",
        #     "name",
        #     "value",
        #     "category",
        #     "quantities",
        #     "description",
        #     "image_product",
        #     "cart",
        #     "user",
        # ]

        read_only_fields = ["id", "user"]


    def create(self, validated_data):
        return Product.objects.create(**validated_data)
