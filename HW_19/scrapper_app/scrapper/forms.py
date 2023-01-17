from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_ids']
        labels = {'product_ids': 'List of products ids:'}
