# store/admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'tracking_number')  # Replace 'user' with the actual field in your Order model

# Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
