from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

"""Database models"""

# class Ingredient(models.Model):
#     """Ingredient for my local recipes"""
#     name = models.CharField(max_length=300)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    """Manager for user creation"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('user must have email address')
        user = self.model(email=self.normalize_email(email) **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return

class User(AbstractBaseUser, PermissionsMixin):
    """User in the database"""
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'