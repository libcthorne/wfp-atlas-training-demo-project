from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    sellable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}: {self.price} (Sellable: {self.sellable})"

    # product = Product(..)
    # assert product.get_label() == "...."


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField()
