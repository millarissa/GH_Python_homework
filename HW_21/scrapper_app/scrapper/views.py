import subprocess
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .forms import ProductForm, AddProductToCart, LoginForm, ProductEdit
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


def page_login(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'my_products.html')
            else:
                messages.error(request, 'Sorry, that login was invalid. Please try again.')
                return render(request, 'login.html', {"form": form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def page_logout(request):
    logout(request)
    return render(request, 'my_products.html')


@user_passes_test(lambda u: u.is_superuser, login_url='/scrapper/my-products/')
def page_delete_product(request, product_id):
    context = {}
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return render(request, 'my_products.html')

    return render(request, 'delete_product.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/scrapper/my-products/')
def page_edit_product(request, product_id):
    context = {}
    product = get_object_or_404(Product, id=product_id)
    form = ProductEdit(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return render(request, 'my_products.html')

    context['form'] = form

    return render(request, "update_product.html", context)

