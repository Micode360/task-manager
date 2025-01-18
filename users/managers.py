from django.contrib.auth.models import BaseUserManager


'''
    What is BaseUserManager?
    BaseUserManager is like a toolbox provided by Django to help you create and manage users in your app.

    It’s the foundation for handling things like:

    Creating regular users.

    Creating superusers (admins).

    Managing passwords and other user-related stuff.
'''

class CustomUserManager(BaseUserManager): # Think of it as a helper that handles creating and managing users in your app.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        if '@' not in email and not email.endswith('.com'):
            raise ValueError('The Email field must be valid')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)