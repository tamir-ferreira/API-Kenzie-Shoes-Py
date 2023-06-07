from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    add_on = models.CharField(max_length=5, blank=True, null=True)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
