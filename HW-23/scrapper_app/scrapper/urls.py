from django.urls import path

from . import views


app_name = 'scrapper'
urlpatterns = [
    path('add-products/', views.page_add_products, name='add_products'),
    path('my-products/', views.page_my_products, name='my_products'),
    path('products/cat/<int:cat_id>', views.page_products_by_cat, name='products_by_cat'),
    path('product/<int:item_id>/', views.page_product, name='product'),
    path('login/', views.page_login, name='login'),
    path('logout/', views.page_logout, name='logout'),
    path('product/<int:product_id>/delete', views.page_delete_product, name='delete_product'),
    path('product/<int:product_id>/edit', views.page_edit_product, name='edit_product'),
    path('api/products/', views.ProductListApi.as_view(), name='api_products_list'),
    path('api/product/<int:product_id>/', views.ProductDetailsApi.as_view(), name='api_products_details'),
    path('api/categories/', views.CategoryListApi.as_view(), name='api_categories_list'),
    path('api/id-srorage/', views.IdStorageListApi.as_view(), name='api_id_storage')
]
