from django.db import models


class Cart(models.Model):
    quantities = models.IntegerField(default=1)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_cart")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="products_cart")