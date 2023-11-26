from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'rating', 'stock_quantity']
    search_fields = ['name', 'category']
    list_filter = ['category', 'rating']
    # Customize other options if needed

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'total_price', 'order_date', 'is_delivered']
    search_fields = ['user__username', 'product__name']
    list_filter = ['order_date', 'is_delivered']
    # Customize other options if needed

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
