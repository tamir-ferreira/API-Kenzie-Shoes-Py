from django.db import models


class Cart(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart",
    )

    product = models.ManyToManyField("products.Product", through="cart.ProductCart", related_name="cart")


class ProductCart(models.Model):
    quantities = models.IntegerField(default=1)
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, related_name="cart_products_list")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="products_cart_list")