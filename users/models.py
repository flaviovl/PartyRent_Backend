from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(('email address'), unique=True, blank=False)
    is_administrator = models.BooleanField('Administrator', default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Client(models.Model):

    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, null=False, default="", max_length=15)
    birth_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='media/client_photo', blank=True, null=True)
