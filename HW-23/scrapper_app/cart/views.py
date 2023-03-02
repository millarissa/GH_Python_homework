from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse

from scrapper.forms import AddProductToCart, ProductDelete # noqa
from scrapper.models import Product # noqa


def view_cart(request):
    cart = request.session.get('cart', {})
    context = {'cart': cart}
    total_sum = 0
    if cart:
        products = Product.objects.filter(id__in=cart.keys()).values()

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
    else:
        context = {
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
        return JsonResponse({'message': 'Product was added to cart', 'cart_quantity': sum(cart.values())})
    else:
        return JsonResponse({'message': 'Form is not valid'}, status=400)


@require_http_methods(['POST'])
def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.save()
    return JsonResponse({'message': 'Cart was cleared', 'cart_quantity': 0, 'total_sum': 0})


@require_http_methods(['POST'])
def delete_product_from_cart(request):
    form = ProductDelete(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart = request.session.setdefault('cart', {})
        del cart[str(data['item_id'])]
        request.session.save()
        return JsonResponse({'message': 'Product was deleted', 'cart_quantity': sum(cart.values())})


@require_http_methods(['POST'])
def change_product_quantity(request):
    change_form = AddProductToCart(request.POST)

    if change_form.is_valid():
        data = change_form.cleaned_data
        cart = request.session.setdefault('cart', {})

        products = Product.objects.filter(id__in=cart.keys()).values()
        products_list = [product for product in products]
        for product in products_list:
            product['quantity'] = cart[str(product['id'])]
            product['sum'] = int(data['quantity']) * int(product['current_price'])

        total_sum = sum([product['sum'] for product in products_list])
        cart[str(data['product_id'])] = data['quantity']
        request.session.save()
        return JsonResponse({
            'message': 'Product`s quantity was changed',
            'cart_quantity': sum(cart.values()),
            'total_sum': total_sum
        })


def cart_quantity(request):
    cart = request.session.get('cart', {})
    return JsonResponse({'cart_quantity': sum(cart.values())})
