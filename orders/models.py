from django.db import models


class OrderStatus(models.TextChoices):
    REALIZADO = "Pedido realizado"
    ANDAMENTO = "Pedido em andamento"
    ENTREGUE = "Pedido entregue"


class UserOrder(models.Model):
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices,
        default=OrderStatus.ANDAMENTO
    )
    buyed_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_order"
    )

    products = models.ForeignKey(
        "products.Product", on_delete=models.PROTECT,
        related_name="products_order"
    )


