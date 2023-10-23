from django.apps import apps
from django.db import models

# Create your models here.
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images', default='product_images/default.svg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def average_rating(self):
        rating_avg = self.productreview_set.aggregate(Avg('rating'))['rating__avg']
        rating_avg = round(rating_avg / 2, 1)
        if rating_avg is not None:
            if (rating_avg * 10) % 10 == 0:
                rating_avg = int(rating_avg)
            self.rating = rating_avg
        else:
            self.rating = 0
        self.save()

    def __str__(self):
        return self.name
