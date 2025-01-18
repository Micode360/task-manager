from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
What is AbstractUser?
AbstractUser is like a blueprint or template for creating custom user models in Django.

Django comes with a built-in system for handling users (like signing up, logging in, etc.), and by default, it uses a basic user model with fields like username, password, email, etc.

But what if you want to add extra fields to your users, like date_of_birth, profile_picture, or phone_number? That’s where AbstractUser comes in!
'''


class User(AbstractUser):
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('assigner', 'Assigner'),
    )

    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=40, choices=ROLE_CHOICES,  blank=False, null=False, default='regular')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email