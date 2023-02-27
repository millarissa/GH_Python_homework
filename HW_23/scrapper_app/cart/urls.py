from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('view-cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('delete-from-cart/', views.delete_product_from_cart, name='delete-from-cart'),
    path('change-cart/', views.change_product_quantity, name='change-cart'),
    path('api/cart-quantity/', views.cart_quantity, name='api-cart-quantity')
]
