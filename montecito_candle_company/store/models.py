from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.CharField(max_length=100, choices=[('candles', 'Candles'), ('home_decor', 'Home Decor'), ('gifts', 'Gifts')])
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} - {self.user.username if self.user else 'Guest'}"
