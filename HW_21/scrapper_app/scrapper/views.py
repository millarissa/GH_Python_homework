import subprocess
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProductForm, AddProductToCart, LoginForm, ProductEdit
from .models import Product, Category


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
    categories = Category.objects.all()
    items_list = Product.objects.all()
    context = {
        "categories": categories,
        'items_list': items_list
    }
    return render(request, "my_products.html", context)


def page_products_by_cat(request, cat_id):
    all_categories = Category.objects.all()
    chosen_category = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category__id=cat_id)
    context = {
        "categories": all_categories,
        'chosen_category': chosen_category,
        'products': products
    }

    return render(request, "products_by_cat.html", context)


def page_product(request, item_id):
    product = get_object_or_404(Product, id=item_id)
    category = Category.objects.get(id=product.category_id)

    form_cart = AddProductToCart(
        initial={'product_id': product.id,
                 'quantity': 1
                 }
    )
    context = {
        'product': product,
        'form': form_cart,
        'category': category
    }

    return render(request, 'product.html', context)


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
                return redirect('/scrapper/my-products/')
            else:
                messages.error(request, 'Sorry, that login was invalid. Please try again.')
                return render(request, 'login.html', {"form": form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def page_logout(request):
    logout(request)
    return redirect('/scrapper/my-products/')


@login_required()
def page_delete_product(request, product_id):
    context = {}
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            product.delete()
            return redirect('/scrapper/my-products/')
    else:
        messages.error(request, 'Wrong access level!')
        return redirect('/scrapper/my-products/')

    return render(request, 'delete_product.html', context)


@login_required()
def page_edit_product(request, product_id):
    context = {}
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=product_id)
        form = ProductEdit(request.POST or None, instance=product)

        if form.is_valid():
            form.save()
            return redirect('/scrapper/my-products/')

        context['form'] = form
    else:
        messages.error(request, 'Wrong access level!')
        return redirect('/scrapper/my-products/')

    return render(request, "edit_product.html", context)
