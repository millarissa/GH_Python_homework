from django import forms
from django.forms import ModelForm, Form
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import IdStorage


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
