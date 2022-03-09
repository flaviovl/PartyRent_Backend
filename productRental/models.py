from datetime import date
from django.db import models
from django.forms import CharField

class Category(models.Model):
    name = models.CharField('CategoryName', max_length=100)

class Comment(models.Model):
    description = CharField('comment', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'), related_name='comments', on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=500)
    picture = models.FileField(upload_to='pictures/')
    active = models.BooleanField(default=True)
    price = models.FloatField(null=False, blank=False, default=0.0)
    like = models.IntegerField(null=False, blank=False, default=0)
    category = models.ManyToManyField(Category, related_name="product_category")

