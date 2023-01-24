from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods


from scrapper.forms import AddProductToCart, ProductDelete # noqa
from scrapper.models import Product # noqa


def view_cart(request):
    cart = request.session.get('cart')
    context = {'cart': cart}
    if cart:
        products = Product.objects.filter(id__in=cart.keys()).values()
        total_sum = ''
        if products:
            products_list = [product for product in products]
            for product in products_list:
                product['quantity'] = cart[str(product['id'])]
                product['sum'] = int(product['quantity']) * int(product['current_price'])
                product['delete_product'] = ProductDelete(
                    initial={'item_id': product['id']}
                )
                product['form_change_cart'] = AddProductToCart(
                    initial={'product_id': product['id'],
                             'quantity': product['quantity']
                             }
                )

            total_sum = sum([product['sum'] for product in products_list])

        context = {'products': products,
                   'cart': cart,
                   'total_sum': total_sum
                   }

    return render(request, 'view_cart.html', context=context)


@require_http_methods(['POST'])
def add_to_cart(request):
    form = AddProductToCart(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart = request.session.setdefault('cart', {})

        cart.setdefault(str(data['product_id']), 0)
        cart[str(data['product_id'])] += data['quantity']

        request.session_modified = True
        request.session.save()
        return redirect(
            reverse('scrapper:product', kwargs={'item_id': data['product_id']})
        )
    else:
        return redirect(reverse('scrapper:my_products'))


@require_http_methods(['POST'])
def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.save()
    return redirect(reverse('cart:view_cart'))


@require_http_methods(['POST'])
def delete_product_from_cart(request):
    form = ProductDelete(request.POST)
    data = form.cleaned_data
    cart = request.session.setdefault('cart', {})
    del cart[str(data['item_id'])]
    request.session.save()
    return redirect(reverse('cart:view_cart'))


@require_http_methods(['POST'])
def change_product_quantity(request):
    change_form = AddProductToCart(request.POST)
    if change_form.is_valid():
        data = change_form.cleaned_data
        cart = request.session.setdefault('cart', {})
        cart[str(data['product_id'])] = data['quantity']
        request.session.save()

    return redirect(reverse('cart:view_cart'))

