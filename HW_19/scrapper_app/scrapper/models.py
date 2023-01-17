from django.db import models


class Product(models.Model):
    product_ids = models.TextField()

    def __str__(self):
        return self.product_ids


class RozetkaItems(models.Model):
    item_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    current_price = models.CharField(max_length=10)
    old_price = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

