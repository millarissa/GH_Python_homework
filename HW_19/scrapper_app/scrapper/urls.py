from django.urls import path

from . import views

urlpatterns = [
    path('add-products/', views.page_add_products, name='add_products'),
    path('my-products/', views.page_my_products, name='my_products'),
    path('product/<int:item_id>/', views.page_product, name='product')
]
