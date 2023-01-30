from django import forms
from django.forms import ModelForm, Form
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import IdStorage, Product


class ProductForm(ModelForm):
    class Meta:
        model = IdStorage
        fields = ['product_ids']
        labels = {'product_ids': 'List of products ids:'}


class AddProductToCart(Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(
        validators=(MinValueValidator(1),
                    MaxValueValidator(20)
                    )
    )


class ProductDelete(Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())


class LoginForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(min_length=4, max_length=20, widget=forms.PasswordInput())


class ProductEdit(ModelForm):
    class Meta:
        model = Product
        fields = [
            'item_id',
            'title',
            'href',
            'current_price',
            'old_price',
            'brand',
            'category',
            'sell_status'
        ]
