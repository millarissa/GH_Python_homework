from django.db import models


class IdStorage(models.Model):
    product_ids = models.TextField()

    def __str__(self):
        return self.product_ids


class Category(models.Model):
    # category_id = models.TextField(max_length=20, default='0'),
    cat_number = models.TextField(max_length=20, default='0'),
    category_title = models.TextField(max_length=50, default='0')


class Product(models.Model):
    item_id = models.CharField(max_length=20, default='No id')
    title = models.CharField(max_length=200, default='No title')
    href = models.CharField(max_length=200, default='No link')
    current_price = models.CharField(max_length=10, default='0')
    old_price = models.CharField(max_length=10, default='0')
    brand = models.CharField(max_length=50, default='No brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='0')
    sell_status = models.CharField(max_length=20, default='Unknown')



