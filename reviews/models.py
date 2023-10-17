from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from products.models import Product
from users.models import Profile


# Create your models here.
class ProductReview(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[
            MinValueValidator(1, "Rating must be at least 1"),
            MaxValueValidator(10, "Rating must be at most 10"),
        ])
    comment = models.TextField(max_length=3000)
    date_created = models.DateTimeField(auto_now_add=True)

''' class Meta:
        unique_together = ('user', 'product')'''

