from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer
from users.models import User
from cart.serializers import CartSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        user = UserSerializer()
        cart = CartSerializer()
        # fields = "__all__"
        fields: [
            "id",
            "name",
            "value",
            "category",
            "quantities",
            "bio",
            "image_product",
            "cart",
            "user",
        ]
        read_only_fields = ["id", "user"]
        exclude = ["cart"]

    def create(self, validated_data):
        user_id = User.objects.get(id=1)
        print(user_id)
        return Product.objects.create(user=user_id, **validated_data)
