# store/urls.py
from django.urls import path
from .views import product_list, add_product, product_detail, category_view

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('categories/<str:category>/', category_view, name='category_view'),
    path('add/', add_product, name='add_product'),
    # Add other URL patterns as needed
]
