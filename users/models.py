from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.db import models
import uuid


# Create your models here.
class Profile(AbstractUser):
    # username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    username = None
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=128)
    p_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


'''class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.CharField(max_length=128)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    amount = models.IntegerField()'''


'''class OrderHistory(models.Model):
    orders = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_history', null=True)'''
