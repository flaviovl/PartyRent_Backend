from datetime import date
from django.db import models
from PartyRental import settings
from userRental.models import User

class Category(models.Model):
    name = models.CharField('CategoryName', max_length=100)

class Comment(models.Model):
    description = models.CharField('Comment', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), related_name='comments', on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=500)
    picture = models.FileField(upload_to='pictures/')
    active = models.BooleanField(default=True)
    price = models.FloatField(null=False, blank=False, default=0.0)
    like = models.IntegerField(null=False, blank=False, default=0)
    category = models.ManyToManyField(Category, related_name="product_category")

class OrderItens(models.Model):
    products = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)

class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    order_itens = models.ManyToManyField(OrderItens, related_name="user_cart")