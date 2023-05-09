from rest_framework import serializers
from .models import *


class ProductCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "quantities", "user_id", "product"]

        read_only_fields = ["id", "user_id", "product"]

