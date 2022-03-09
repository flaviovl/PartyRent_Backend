import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    nome = models.CharField(('name'), max_length=50, blank=True)
    email = models.EmailField(('email address'), unique=True)
    picture = models.FileField(('picture'), blank=True, default='member-default.png')
    phonenumber = models.CharField(max_length=20, blank=True)
    password_confirmation = models.CharField(('password confirmation'), max_length=128)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    recipient_id = models.CharField(max_length=300, null=True)
    player_id = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

User._meta.get_field('username')._unique = False