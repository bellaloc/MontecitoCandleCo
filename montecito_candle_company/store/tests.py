# store/tests.py
from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Candle', description='A scented candle', price=15.99)
        Product.objects.create(name='Lantern', description='An elegant lantern', price=29.99)

    def test_products_have_valid_prices(self):
        """Test that product prices are non-negative."""
        candle = Product.objects.get(name='Candle')
        lantern = Product.objects.get(name='Lantern')

        self.assertGreaterEqual(candle.price, 0)
        self.assertGreaterEqual(lantern.price, 0)

    def test_product_names_are_unique(self):
        """Test that product names are unique."""
        candle = Product.objects.get(name='Candle')
        lantern = Product.objects.get(name='Lantern')

        # Try to create a new product with the same name as 'Candle'
        new_candle = Product(name='Candle', description='Another scented candle', price=19.99)
        with self.assertRaises(Exception):
            new_candle.save()

        # Try to create a new product with a different name
        new_lantern = Product(name='New Lantern', description='A new lantern', price=39.99)
        new_lantern.save()

        self.assertEqual(Product.objects.count(), 2)

# Add more tests as needed
