from rest_framework import serializers
from .models import *


class ProductCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "quantities", "user", "product"]

        # depth = 1 

        read_only_fields = ["id", "user", "product"]

