from django.db import models


class OrderStatus(models.TextChoices):
    REALIZADO = "Realizado"
    ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"


class UserOrder(models.Model):
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices,
        default=OrderStatus.REALIZADO
    )
    buyed_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_order"
    )

    products = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE,
        related_name="products_order"
    )


