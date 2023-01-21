from django.forms import ModelForm
from .models import IdStorage


class ProductForm(ModelForm):
    class Meta:
        model = IdStorage
        fields = ['product_ids']
        labels = {'product_ids': 'List of products ids:'}
