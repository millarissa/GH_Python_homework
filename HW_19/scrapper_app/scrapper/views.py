from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Product, RozetkaItems
from .rozetka_operations import data_operations, rozetka_api


def page_add_products(request):
    form = ProductForm()
    if request.method == 'POST':
        text = request.POST.get('product_ids')
        for i in text.split('\n'):
            modified = request.POST.copy()
            modified['product_ids'] = i
            form = ProductForm(modified)
            form.save()
            save_rozetka_items(i)
    else:
        form = ProductForm()
    return render(request, 'add_products.html', {'form': form})


def page_my_products(request):
    items_list = RozetkaItems.objects.all()
    return render(request, "my_products.html", {'items_list': items_list})


def page_product(request, item_id):
    product = get_object_or_404(RozetkaItems, id=item_id)
    return render(request, 'product.html', {'product': product})


def save_rozetka_items(item_id):
    database = data_operations.DataBaseOperations()
    rozetka = rozetka_api.RozetkaAPI()

    rosetka_item_values = rozetka.get_item_data(item_id)
    if rosetka_item_values:
        database.insert_items(rosetka_item_values)
