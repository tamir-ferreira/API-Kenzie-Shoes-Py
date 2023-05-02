from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False, null=True, blank=True)
    image_user = models.URLField(max_length=200)

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="address_user",
    )


class OrderStatus(models.TextChoices):
    REALIZADO = "Pedido realizado"
    ANDAMENTO = "Pedido em andamento"
    ENTREGUE = "Pedido entregue"


class UserOrder(models.Model):
    status = models.CharField(max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.ANDAMENTO)
    buyed_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_order"
    )