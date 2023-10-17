import uuid

from django.db import models

# Create your models here.
from products.models import Product
from users.models import Profile


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=100, default="Pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

