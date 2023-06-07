from django.db import models

# Create your models here.

class Ingredient(models.Model):
    """Ingredient for my local recipes"""
    name = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)