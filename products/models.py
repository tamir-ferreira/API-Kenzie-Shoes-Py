from django.db import models


class Category(models.TextChoices):
    BOTAS = "Botas",
    CHINELOS_SANDALIAS = "Chinelos e Sandálias",
    CHUTEIRAS = "Chuteiras",
    SAPATENIS = "Sapatênis",
    TENIS = "Tênis",
    TENIS_CORRIDA = "Tênis de corrida",


class Product(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=Category.choices,
                                default=Category.BOTAS)
    quantities = models.IntegerField(default=0)
    bio = models.TextField()
    image_product = models.URLField(max_length=200)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_product",
    )

    cart = models.ManyToManyField("cart.Cart", related_name="cart")