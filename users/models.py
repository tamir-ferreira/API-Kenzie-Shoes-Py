from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False, null=True, blank=True)
    image_user = models.URLField(max_length=200, null=True, blank=True)

    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="address",
    )

    product = models.ManyToManyField("products.Product", through="cart.Cart", related_name="cart")