from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer
from cart.serializers import ProductCartSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        user = UserSerializer
        cart = ProductCartSerializer
        fields = [
            "id",
            "name",
            "value",
            "category",
            "stock",
            "description",
            "image_product",
            "user",
        ]

        read_only_fields = ["id", "user"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


# class ProductOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         user = UserOrderSerializer
#         fields = [
#             "id",
#             "name",
#             "value",
#             "category",
#             "description",
#             "stock",
#             "image_product",
#             "user",
#         ]
      
#         read_only_fields = ["id", "user"]
#         exclude = ["stock"]