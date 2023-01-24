import subprocess
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, AddProductToCart
from .models import Product


def page_add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product_ids = request.POST.get('product_ids')
        form.save()
        process = subprocess.Popen(['python', 'scrapper/rozetka_operations/save_items.py', product_ids])
        process.communicate()
    else:
        form = ProductForm()
    return render(request, 'add_products.html', {'form': form})


def page_my_products(request):
    items_list = Product.objects.all()
    return render(request, "my_products.html", {'items_list': items_list})


def page_product(request, item_id):
    product = get_object_or_404(Product, id=item_id)
    form_cart = AddProductToCart(
        initial={'product_id': product.id,
                 'quantity': 1
                 }
    )
    return render(request, 'product.html', {'product': product, 'form': form_cart})

