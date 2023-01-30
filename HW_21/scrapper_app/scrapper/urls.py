from django.urls import path

from . import views

app_name = 'scrapper'
urlpatterns = [
    path('add-products/', views.page_add_products, name='add_products'),
    path('my-products/', views.page_my_products, name='my_products'),
    path('product/<int:item_id>/', views.page_product, name='product'),
    path('login/', views.page_login, name='login'),
    path('logout/', views.page_logout, name='logout'),
    path('product/<int:product_id>/delete', views.page_delete_product, name='delete_product'),
    path('product/<int:product_id>/edit', views.page_edit_product, name='edit_product')
]
