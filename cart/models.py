from decimal import Decimal

from django.db import models

from products.models import Product
from users.models import Profile

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Product, through='CartItem')
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_totals(self):
        # Logic to update total_quantity and total_price based on the cart items
        # This can be implemented in a method or overridden save() method
        items = self.cartitem_set.all()
        total_quantity = 0
        total_price = Decimal('0.00')

        for item in items:
            total_quantity += item.quantity
            total_price += item.subtotal

        self.total_quantity = total_quantity
        self.total_price = total_price
        self.save()

    def __str__(self):
        return f"Cart #{self.pk} - User: {self.user}"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_subtotal(self):
        self.subtotal = Decimal(self.price) * Decimal(self.quantity)

    def update_price(self):
        self.price = self.product.price
        self.save()

    def __str__(self):
        return f"CartItem #{self.pk} - Cart: {self.cart} - Product: {self.product}"

'''    def save(self,  *args, **kwargs):
        if not self.price:  # Only set the price if it's not already set
            self.update_price()
        self.update_subtotal()
        super().save(*args, **kwargs)
        self.cart.update_totals()  # Update the cart totals after saving the cart item'''