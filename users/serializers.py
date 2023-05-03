from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from addresses.serializers import AddressSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # address = serializers.PrimaryKeyRelatedField(read_only=True)
    address_id = serializers.IntegerField(source="address.id")

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def create(self, validated_data: dict) -> User:
        print("=" * 150)
        print(validated_data)
        address_create = validated_data.pop("address")
        user = User.objects.create_user(**validated_data)
        Address.objects.create(user=user, **address_create)

        # return User.objects.create_superuser(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_seller",
            "image_user",
            "address_id",
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
